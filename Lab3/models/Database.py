import psycopg2
from psycopg2 import Error
from .PlantException import PlantException
from .Plant import Plant

class Database:
    def __init__(self, db_host, db_name, db_user, db_password):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host=db_host,
                database=db_name,
                user=db_user,
                password=db_password
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS plants (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    species TEXT NOT NULL,
                    watering_date TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except Error as e:
            raise PlantException(f"Ошибка подключения к базе данных: {e}")

    def add_plant(self, plant):
        try:
            self.cursor.execute("INSERT INTO plants (name, species, watering_date) VALUES (%s, %s, %s)",
                                (plant.name, plant.species, plant.watering_date))
            self.conn.commit()
        except Error as e:
            raise PlantException(f"Ошибка добавления растения в базу данных: {e}")

    def get_plants(self):
        try:
            self.cursor.execute("SELECT * FROM plants")
            return self.cursor.fetchall()
        except Error as e:
            raise PlantException(f"Ошибка чтения данных из базы данных: {e}")
        
    def get_care(self):
        try:
            self.cursor.execute("SELECT * FROM care")
            return self.cursor.fetchall()
        except Error as e:
            raise PlantException(f"Ошибка чтения данных из базы данных: {e}")
        
    def get_watering(self):
        try:
            self.cursor.execute("SELECT * FROM waterings")
            return self.cursor.fetchall()
        except Error as e:
            raise PlantException(f"Ошибка чтения данных из базы данных: {e}")