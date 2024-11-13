import concurrent.futures

class Task1:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    # Простая реализация генератора
    def simple_generator(self):
        for i in range(self._a, self._b + 1):
            yield abs(i)

    # Метод для получения первых n значений из генератора
    def get_first(self, n):
        generator = self.simple_generator()
        first_numbers = [next(generator) for _ in range(n)]
        return first_numbers

    # Параллельная реализация с использованием ThreadPoolExecutor
    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_first, n)
            return future.result()