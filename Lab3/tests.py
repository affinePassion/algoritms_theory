import tests
import pytest
from models import Plant, Database, Care

@pytest.fixture
def plant():
    return Plant(name = "Test Plant" , species = "Test Species", watering_date = "2024-11-12", amount_waterings = 0)

def test_Plant_init(plant):
    assert plant.name == "Test Plant"
    assert plant.species == "Test Species"
    assert plant.watering_date == "2024-11-12"
    assert plant.amount_waterings == 0

def test_Plant_setters(plant):
    plant.name = 'New Name'
    plant.species = 'New Species'
    plant.watering_date = '2024-11-13'
    plant.amount_waterings = 1
    assert plant.name == 'New Name'
    assert plant.species == 'New Species'
    assert plant.watering_date == '2024-11-13'
    assert plant.amount_waterings == 1

def test_Plant_str(plant):
    assert str(plant) == "Растение: Test Plant ,\n Вид: Test Species,\n Последняя дата полива: 2024-11-12,\n Количество поливов: 0 "

@pytest.fixture
def care():
    return Care(plant_id = 1, care_date = "2024-11-12", care_type = "Watering", notes = "Test notes")

def test_Care_init(care):
    assert care.plant_id == 1
    assert care.care_date == '2024-11-12'
    assert care.care_type == 'Watering'
    assert care.notes == 'Test notes'

def test_Care_setters(care):
    care.plant_id = 2
    care.care_date = '2024-11-13'
    care.care_type = 'Fertilizing'
    care.notes = 'New notes'
    assert care.plant_id == 2
    assert care.care_date == '2024-11-13'
    assert care.care_type == 'Fertilizing'
    assert care.notes == 'New notes'

def test_Care_str(care):
    assert str(care) == "Растение: 1 ,\n Тип ухода: Watering,\n Дата ухода: 2024-11-12,\n Описание: Test notes "

@pytest.fixture
def db_connection():
    return Database(db_host = "povt-cluster.tstu.tver.ru", db_name = "plantSystem", db_user = "mpi", db_password = "135a1")

def test_Database_init(db_connection):
    assert db_connection.conn is not None

def test_Database_add_plant(db_connection, plant):
    db_connection.add_plant(plant)
    db_connection.cursor.execute("SELECT * FROM plants WHERE name = %s", (plant.name,))
    result = db_connection.cursor.fetchone()
    assert result is not None

def test_Database_get_plants(db_connection, plant):
    db_connection.add_plant(plant)
    plants = db_connection.get_plants()
    assert len(plants) > 0

def test_Database_get_care(db_connection):
    # Ensure the 'care' table exists and has some data
    db_connection.cursor.execute("""
        CREATE TABLE IF NOT EXISTS care (
            id SERIAL PRIMARY KEY,
            plant_id INTEGER NOT NULL,
            care_date TEXT NOT NULL,
            care_type TEXT NOT NULL,
            notes TEXT
        )
    """)
    db_connection.conn.commit()
    care = Care(1, '2024-11-12', 'Watering', 'Test notes')
    db_connection.cursor.execute("INSERT INTO care (plant_id, care_date, care_type, notes) VALUES (%s, %s, %s, %s)",
                                  (care.plant_id, care.care_date, care.care_type, care.notes))
    db_connection.conn.commit()
    care_data = db_connection.get_care()
    assert len(care_data) > 0

def test_Database_get_waterings(db_connection, plant):
    db_connection.add_plant(plant)
    waterings = db_connection.get_waterings()
    assert len(waterings) > 0