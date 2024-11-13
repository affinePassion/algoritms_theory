import concurrent.futures

class Task3:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def multiply_generator(self):
    # Используем zip и map для парного перемножения
        products = map(lambda pair: pair[0] * pair[1], zip(self.list1, self.list2))
        for product in products:
            yield product

    # Метод для получения первых n значений генератора
    def get_first_products(self, n):
        generator = self.multiply_generator()
        return [next(generator) for _ in range(n)]

    # Параллельная реализация с использованием ThreadPoolExecutor
    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_first_products, n)
            return future.result()