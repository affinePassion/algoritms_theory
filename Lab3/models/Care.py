class Care:
    def __init__(self, plant_id, care_date, care_type, notes):
        self._plant_id = plant_id
        self._care_date = care_date
        self._care_type = care_type
        self._notes = notes

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, value):
        self._plant_id = value

    @property
    def care_date(self):
        return self._care_date

    @care_date.setter
    def care_date(self, value):
        self._care_date = value

    @property
    def care_type(self):
        return self._care_type

    @care_type.setter
    def care_type(self, value):
        self._care_type = value

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, value):
        self._notes = value

    def __str__(self):
        return (f"Растение: {self._plant_id} ,\n Тип ухода: {self._care_type},\n Дата ухода: {self._care_date},\n Описание: {self._notes} ")