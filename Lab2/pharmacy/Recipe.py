from .Pharmacy import Pharmacy
from .Pacient import Pacient
from .Preparation import Preparation

# Класс Рецепт
class Recipe(Pharmacy):
    def __init__(self, pacient : Pacient, preparations : {Preparation.name, Preparation.quantity, Preparation.price} = None):
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

    def calculate_cost(self):
        total_cost = 0
        for prep in self.preparations:
            total_cost += prep['price'] * prep['quantity']
        return total_cost
    
    def calculate_stock(self):
        stock = {}
        for prep in self.preparations:
            stock[prep['name']] = prep['quantity']
        return stock

    def __str__(self):
        prep_str = ", ".join(f"{prep['name']}, {prep['quantity']}шт, {prep['price']}руб\n" for prep in self.preparations)
        return f"Рецепт для пациента {self.pacient.name}: {prep_str}\nЕго итоговая стоимость = {self.calculate_cost} руб\nЧисло лекарств = {self.calculate_cost}шт"
