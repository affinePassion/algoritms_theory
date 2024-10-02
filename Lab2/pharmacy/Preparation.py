from .Pharmacy import Pharmacy

# Класс Лекарство
class Preparation(Pharmacy):

    def __init__(self, name : str, price : float, quantity : int):
        self.name = name
        self.price = price
        if quantity < 0:
            raise ValueError("Количество лекарств не может быть отрицательным")
        self.quantity = quantity

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строковым значением")
        self.name = value
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Цена лекарства должна задаваться числом")
        self.price = value

    @property
    def quantity(self):
        return self.quantity
    
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество лекарств должно задаваться целым числом")
        self.quantity = value

    def calculate_cost(self):
        total_cost = self.quantity * self.price
        return total_cost
    
    def calculate_stock(self):
        pass
    
    def __str__(self):
        return f"Лекарство: {self.name} в количестве {self.quantity}шт стоит {self.calculate_cost()}"
    
    
    


