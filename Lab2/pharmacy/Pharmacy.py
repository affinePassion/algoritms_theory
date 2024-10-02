from abc import ABC, abstractmethod

# Абстрактный класс Аптека
class Pharmacy(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass
    
    @abstractmethod
    def calculate_stock(self):
        pass

    def __str__(self):
        return "Аптека"
    