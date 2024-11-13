import concurrent.futures
import random
from string import ascii_lowercase, ascii_uppercase

class Task2:
    def __init__(self, chars):
        self.chars = chars

    # Функция-генератор для генерации паролей
    def password_generator(self):
        while True:
            password = ''.join(random.choice(self.chars) for _ in range(12))
            yield password

    def get_first(self, n):
        generator = self.password_generator()
        return [next(generator)for _ in range(n)]

    def parallel_execution(self, n):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_first, n)
            return future.result()