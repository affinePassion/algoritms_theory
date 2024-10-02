from .Pharmacy import Pharmacy

# Класс пациент
class Pacient(Pharmacy):
    def __init__(self, name : str):
        self.name = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно задаваться строкой")
        self.name = value

    def calculate_cost(self):
        return 0
    
    def calculate_stock(self):
        pass

    def __str__(self):
        return f"Пациент: {self.name}"