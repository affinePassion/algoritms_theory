from .Pharmacy import Pharmacy

# Класс пациент
class Pacient(Pharmacy):
    def __init__(self, name : str):
        if not isinstance(name, str):
            raise ValueError("ФИО пациента должно задаваться строкой")
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    def calculate_cost(self):
        raise NotImplementedError("Method calculate_cost is not implemented")

    def calculate_stock(self):
        raise NotImplementedError("Method calculate_stock is not implemented")

    def __str__(self):
        return f"Пациент: {self.name}"