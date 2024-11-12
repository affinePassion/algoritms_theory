class Plant:
    def __init__(self, name, species, watering_date):
        self._name = name
        self._species = species
        self._watering_date = watering_date

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self,value):
        self._species = value
    
    @property
    def watering_date(self):
        return self._watering_date
    
    @watering_date.setter
    def watering_date(self,value):
        self._watering_date = value

    def __str__(self):
        return (f"Растение: {self._name} ,\n Вид: {self._species},\n Дата полива: {self._watering_date},\n ")