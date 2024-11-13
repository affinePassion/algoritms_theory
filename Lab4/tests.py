import pytest
from tasks import Task1, Task2, Task3
from string import ascii_lowercase, ascii_uppercase

class TestTask1:
    def test_number_generator(self):
        task = Task1(-1000, -998)
        numbers = list(task.simple_generator())
        assert numbers == [1000, 999, 998]

    def test_get_first(self):
        task = Task1(-100, 456)
        first_numbers = task.get_first(5)
        assert first_numbers == [100, 99, 98, 97, 96]

    def test_parallel_execution(self):
        task = Task1(-1000, 3)
        result = task.parallel_execution(5)
        assert result == [1000, 999, 998, 997, 996]


class TestTask3:
    def test_float_generator(self):
        task = Task3(eval("1, 2, 3"), eval("4, 5, 6"))
        float_numbers = list(task.get_first_products(3))
        assert float_numbers == list([4, 10, 18])

    def test_get_first_floats(self):
        task = Task3(eval("-1, 10, 24, 2"), eval("1000, 4, 5, 0"))
        first_floats = list(task.get_first_products(3))
        assert first_floats == list([-1000, 40, 120])

    def test_parallel_execution(self):
        task = Task3(eval("-1, 10, 24, 2"), eval("1000, 4, 5, 0"))
        result = task.parallel_execution(4)
        assert result == list([-1000, 40, 120, 0])
