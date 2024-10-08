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
        print("7. Рассчитать запас лекарств")
        print("8. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                newPrep = input("Введите название, цену(вещественным числом) и количество лекарства через пробел: ").split()
                float(newPrep[1])
                int(newPrep[2])
            except ValueError:
                print("Ошибка в создании лекарства")
                continue
            if(float(newPrep[1]) <= 0 or int(newPrep[2]) <= 0):
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

            pacients.append(Pacient(pacient))
            result = f"{pacient} создан."
            print(result)

        elif choice == "3":
            if len(pacients) < 1 or len(preparations) < 1:
                print("Для создания рецепта необходимо наличие как минимум одного пациента или препарата.")
                continue

            print("Доступные пациенты: ")
            for i, pac in enumerate(pacients):
                print(f"{i+1}. {pac.name}")
            try:
                pacient_choice = int(input("Выберите пациента: ")) - 1
            except ValueError:
                print("Ошибка в создании пациента")
                continue

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
            
            rec_cost = 0

            for i, rec in enumerate(recipes):
                if rec.pacient == pacients[pacient_choice]:
                    rec_cost = rec.calculate_cost()
                    print(rec.calculate_cost())

            
            
            save_choice = input("Сохранить результат в word?(Yes/No): ")
            if save_choice=="Yes":
                save_docs(f"Стоимость рецепта для пациента: {pacients[pacient_choice].name} составляет {rec_cost} руб",
                           f"Стоимость рецепта для {pacients[pacient_choice].name}")
                

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
                    print(f"Количество лекарств в рецепте {rec.calculate_stock()[1]}")

        elif choice == "6":
            if not preparations:
                print("Список лекарств пуст.")
            print_str = ""
            for p in preparations:
                print_str += str(p) + "\n"
                print(p)
            save_choice = input("Сохранить результат в word?(Yes/No): ")
            if save_choice=="Yes":
                save_docs(print_str, "Лекарства")

        elif choice == "7":
            print(f"Общее кол-во лекарств = {Preparation.get_total_quantity()}")
            save_choice = input("Сохранить результат в word?(Yes/No): ")
            if save_choice=="Yes":
                save_docs(f"Общее кол-во лекарств = {Preparation.get_total_quantity()}",
                           "Расчет запаса лекарств")

        elif choice == "8":
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