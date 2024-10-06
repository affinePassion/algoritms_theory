from pprint import pprint
import os
from pharmacy import Pacient, Preparation, Recipe
from docx import Document


def main():
    preparations = []
    pacients = []
    recipes = []
    while True:
        print("\nMenu:")
        print("1. Создать лекарство")
        print("2. Создать пациента")
        print("3. Создать рецепт для пациента")
        print("4. Рассчитать стоимость рецепта для пациента")
        print("5. Рассчитать кол-во лекарств в рецепте")
        print("6. Отобразить все лекарства")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            newPrep = input("Введите название, цену(вещественным числом) и количество лекарства через пробел: ").split()
            if((type(newPrep[1]) != float) or type(newPrep[2]) != int):
                print("Ошибка в создании лекарства")
                continue
            if(newPrep[1] <= 0 or newPrep[2] <= 0):
                print("Ошибка в создании лекарства")
                continue
            preparation = Preparation(newPrep[0], float(newPrep[1]), int(newPrep[2]))
            preparations.append(preparation)
            result = f"Лекарство {newPrep[0]} создано."
            print(result)


        elif choice == "2":
            pacient = input("Введите ФИО пациента: ")
            if(len(pacient.split()) != 3):
                print("Ошибка в создании пациента. Возможно, вы ввели неполное ФИО")
                continue
            pacients.append(pacient)
            result = f"{pacient} создан."
            print(result)

        elif choice == "3":
            if len(pacients) < 1 or len(preparations) < 1:
                print("Для создания рецепта необходимо наличие как минимум одного пациента или препарата.")
                continue

            print("Доступные пациенты: ")
            for i, pac in enumerate(pacients):
                print(f"{i+1}. {pac.name}")

            pacient_choice = int(input("Выберите пациента: ")) - 1

            if pacient_choice < 0 or pacient_choice >= len(pacients):
                print("Ошибка при выборе пациента.")
                continue

            print("Доступные препараты: ")
            for i, prep in enumerate(preparations):
                print(f"{i+1}. {prep.name}")

            preparations_choice = input("Выберите препараты(если вы хотите выбрать несколько лекарств, введите номера лекарств через пробел(например: 1 3 4)): ").split()
            preps = []
            for i in range(len(preparations_choice)):
                preps.append(preparations[int(preparations_choice[i]) - 1])
            

            recipe = Recipe(pacients[pacient_choice], preps)
            recipes.append(recipe)
            result=f"Рецепт для {pacients[pacient_choice]} создан"
            print(recipe)

        elif choice == "4":
            if(len(pacients) <= 0 or len(recipes) <= 0):
                print("Ошибка. Список пациентов пуст, соответственно и список рецептов тоже.")
                continue

            print("Доступные пациенты: ")
            for i, pac in enumerate(pacients):
                print(f"{i+1}. {pac.name}")

            pacient_choice = int(input("Выберите пациента: ")) - 1

            if pacient_choice < 0 or pacient_choice >= len(pacients):
                print("Ошибка при выборе пациента.")
                continue

            for i, rec in enumerate(recipes):
                if rec.pacient == pacients[pacient_choice]:
                    print(rec.calculate_cost())
                

        elif choice == "5":
            if len(recipes) < 1:
                print("Список рецептов пуст.")
                continue

            print("Доступные рецепты: ")
            for i, rec in enumerate(recipes):
                print(f"{i+1}. {rec.pacient}")

            recipe_choice = int(input("Выберите рецепт: ")) - 1

            if recipe_choice < 0 or recipe_choice >= len(recipes):
                print("Ошибка при выборе рецепта.")
                continue

            for i, rec in enumerate(recipes):
                if recipe_choice == i:
                    print(f"Стоимость рецепта составляет {rec.calculate_stock()[1]} руб")

        elif choice == "6":
            if not preparations:
                print("Список лекарств пуст.")
            for p in preparations:
                print(p)

        elif choice == "7":
            print("Выход.")
            break
        
        else:
            print("Ошибка. Выберите номер из списка")

def save_docs(result, nameDoc):
    doc = Document()
    doc.add_paragraph(result)
    doc.save(f"{nameDoc}.docx")
    print("Файл сохранен")

if __name__ == "__main__":
    main()