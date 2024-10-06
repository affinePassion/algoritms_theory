from typing import List
from .Pharmacy import Pharmacy
from .Pacient import Pacient
from .Preparation import Preparation

# Класс Рецепт
class Recipe(Pharmacy):
    def __init__(self, pacient : Pacient, preparations: List[Preparation] = None):
        self._pacient = pacient
        self._preparations = preparations if preparations else []

    @property
    def pacient(self):
        return self._pacient

    @pacient.setter
    def pacient(self, value):
        self._pacient = value

    @property
    def preparations(self):
        return self._preparations
    
    @preparations.setter
    def preparations(self, value):
        self._preparations = value

    @classmethod
    def add_preparation(self, prep : Preparation):
        self._preparations.append(prep)

    @classmethod
    def calculate_cost(self):
        total_cost = 0
        for prep in self._preparations:
            total_cost += prep._price * prep._quantity
        return total_cost
    
    @classmethod
    def calculate_stock(self):
        stock = {}
        for prep in self._preparations:
            stock[prep._name] = prep._quantity
        return (stock, sum(stock.values()))

    def __str__(self):
        recipe_string = f"Рецепт для пациента {self.pacient.name}:\n"
        for prep in self.preparations:
            recipe_string += f"{prep.name} {prep.price:.2f}руб х {prep.quantity}шт\n"
        return recipe_string