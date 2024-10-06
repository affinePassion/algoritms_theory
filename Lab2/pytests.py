import pytest
from pharmacy.Pacient import Pacient
from pharmacy.Preparation import Preparation
from pharmacy.Recipe import Recipe

class Test_Pacient:
    def test_pacient_init(self):
        # Тест инициализации пациента
        pacient = Pacient("Иванов Иван Иванович")
        assert pacient.name == "Иванов Иван Иванович"

    def test_pacient_name_property(self):
        # Тест свойства name
        pacient = Pacient("Иванов Иван Иванович")
        assert pacient.name == "Иванов Иван Иванович"
        pacient.name = "Петров Петр Петрович"
        assert pacient.name == "Петров Петр Петрович"

    def test_pacient_name_invalid_type(self):
        # Тест на невалидный тип имени
        with pytest.raises(ValueError):
            Pacient(123)


    def test_pacient_str_representation(self):
        # Тест строкового представления объекта
        pacient = Pacient("Иванов Иван Иванович")
        assert str(pacient) == "Пациент: Иванов Иван Иванович"

    def test_pacient_methods(self):
        pacient = Pacient("Иванов Иван Иванович")
        with pytest.raises(NotImplementedError):
            pacient.calculate_cost()
        with pytest.raises(NotImplementedError):
            pacient.calculate_stock()

class Test_Preparation:
    def test_preparation_init(self):
        # Тест инициализации объекта Preparation
        prep = Preparation("Лекарство1", 100.0, 10)
        assert prep.name == "Лекарство1"
        assert prep.price == 100.0
        assert prep.quantity == 10

    def test_preparation_init_invalid_quantity(self):
        # Тест инициализации с невалидным количеством
        with pytest.raises(ValueError):
            Preparation("Лекарство1", 100.0, -10)

    def test_preparation_name_property(self):
        # Тест свойства name
        prep = Preparation("Лекарство1", 100.0, 10)
        assert prep.name == "Лекарство1"
        prep.name = "Лекарство2"
        assert prep.name == "Лекарство2"

    def test_preparation_name_invalid_type(self):
        # Тест на невалидный тип имени
        prep = Preparation("Лекарство1", 100.0, 10)
        with pytest.raises(ValueError):
            prep.name = 123

    def test_preparation_price_property(self):
        # Тест свойства price
        prep = Preparation("Лекарство1", 100.0, 10)
        assert prep.price == 100.0
        prep.price = 200.0
        assert prep.price == 200.0

    def test_preparation_price_invalid_type(self):
        # Тест на невалидный тип цены
        prep = Preparation("Лекарство1", 100.0, 10)
        with pytest.raises(ValueError):
            prep.price = "200"

    def test_preparation_quantity_property(self):
        # Тест свойства quantity
        prep = Preparation("Лекарство1", 100.0, 10)
        assert prep.quantity == 10
        prep.quantity = 20
        assert prep.quantity == 20

    def test_preparation_quantity_invalid_type(self):
        # Тест на невалидный тип количества
        prep = Preparation("Лекарство1", 100.0, 10)
        with pytest.raises(ValueError):
            prep.quantity = "20"

    def test_preparation_calculate_cost(self):
        # Тест метода calculate_cost
        prep = Preparation("Лекарство1", 100.0, 10)
        assert prep.calculate_cost() == 1000.00

    def test_preparation_calculate_stock(self):
        # Тест метода calculate_stock (должен вызывать исключение, если не реализован)
        prep = Preparation("Лекарство1", 100.0, 10)
        with pytest.raises(NotImplementedError):
            prep.calculate_stock()

    def test_preparation_get_total_quantity(cls):
        # Тест статического метода get_total_quantity
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        assert Preparation.get_total_quantity() == 130

    def test_preparation_total_quantity_update(self):
        # Тест обновления общего количества при изменении количества у объекта
        prep = Preparation("Лекарство1", 100.0, 10)
        assert Preparation.get_total_quantity() == 140
        prep.quantity = 20
        assert Preparation.get_total_quantity() == 150

class Test_Recipe:
    def test_recipe_init(self):
        # Тест инициализации объекта Recipe
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe = Recipe(pacient, [prep1, prep2])
        assert recipe.pacient.name == "Иванов Иван Иванович"
        assert len(recipe.preparations) == 2
        assert len(recipe._recipe_preparations) == 2

    def test_recipe_init_without_preparations(self):
        # Тест инициализации без препаратов
        pacient = Pacient("Иванов Иван Иванович")
        recipe = Recipe(pacient)
        assert recipe.pacient.name == "Иванов Иван Иванович"
        assert len(recipe.preparations) == 0
        assert len(recipe._recipe_preparations) == 0

    def test_recipe_pacient_property(self):
        # Тест свойства pacient
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        recipe = Recipe(pacient, [prep1])
        assert recipe.pacient.name == "Иванов Иван Иванович"
        new_pacient = Pacient("Петров Петр Петрович")
        recipe.pacient = new_pacient
        assert recipe.pacient.name == "Петров Петр Петрович"

    def test_recipe_preparations_property(self):
        # Тест свойства preparations
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe = Recipe(pacient, [prep1])
        assert len(recipe.preparations) == 1
        recipe.preparations = [prep1, prep2]
        assert len(recipe.preparations) == 2
        assert len(recipe._recipe_preparations) == 2

    def test_recipe_add_preparation(self):
        # Тест метода add_preparation
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        recipe = Recipe(pacient, [prep1])
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe.add_preparation(prep2)
        assert len(recipe.preparations) == 2
        assert len(recipe._recipe_preparations) == 2

    def test_recipe_calculate_cost(self):
        # Тест метода calculate_cost
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe = Recipe(pacient, [prep1, prep2])
        assert recipe.calculate_cost() == 100.0 + 200.0

    def test_recipe_calculate_stock(self):
        # Тест метода calculate_stock
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe = Recipe(pacient, [prep1, prep2])
        stock, total = recipe.calculate_stock()
        assert stock == {"Лекарство1": 1, "Лекарство2": 1}
        assert total == 2

    def test_recipe_str_representation(self):
        # Тест строкового представления объекта
        pacient = Pacient("Иванов Иван Иванович")
        prep1 = Preparation("Лекарство1", 100.0, 10)
        prep2 = Preparation("Лекарство2", 200.0, 20)
        recipe = Recipe(pacient, [prep1, prep2])
        expected_string = f"Рецепт для пациента Иванов Иван Иванович:\nЛекарство1 100.00руб х 1шт\nЛекарство2 200.00руб х 1шт\n"
        assert str(recipe) == expected_string