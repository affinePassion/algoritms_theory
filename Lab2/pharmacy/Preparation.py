from .Pharmacy import Pharmacy

# Класс Лекарство
class Preparation(Pharmacy):

    def __init__(self, name : str, price : float, quantity : int):
        self._name = name
        self._price = price
        if quantity < 0:
            raise ValueError("Количество лекарств не может быть отрицательным")
        self._quantity = quantity

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строковым значением")
        self._name = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Цена лекарства должна задаваться числом")
        self._price = value

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество лекарств должно задаваться целым числом")
        self._quantity = value

    def calculate_cost(self):
        total_cost = round(self.quantity * self.price, 2)
        return total_cost
    
    @classmethod
    def calculate_stock(self):
        pass
    
    def __str__(self):
        return f"Лекарство↓\nНазвание: {self.name}\nКол-во: {self.quantity}шт\nСтоимость(1 шт): {self.price} руб\nИтоговая стоимость: {self.calculate_cost()} руб\n"
    
    
    


