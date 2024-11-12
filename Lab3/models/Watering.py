class Watering:
    def __init__(self, plant_id, watering_date, notes):
        self._plant_id = plant_id
        self._watering_date = watering_date
        self._notes = notes

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, value):
        self._plant_id = value

    @property
    def watering_date(self):
        return self._watering_date

    @watering_date.setter
    def watering_date(self, value):
        self._watering_date = value

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        self._notes = value

    def __str__(self):
        return (f"Растение: {self._plant_id} ,\n Дата полива: {self._watering_date},\n Описание: {self._notes},\n ")