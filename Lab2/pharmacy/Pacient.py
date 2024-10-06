from .Pharmacy import Pharmacy

# Класс пациент
class Pacient(Pharmacy):
    def __init__(self, name : str):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("ФИО пациента должно задаваться строкой")
        self._name = value

    def calculate_cost(self):
        pass

    def calculate_stock(self):
        pass

    def __str__(self):
        return f"Пациент: {self.name}"