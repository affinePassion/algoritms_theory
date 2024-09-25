import importlib

def main():
    tasks = {
        1: 'tasks.00_distance',
        2: 'tasks.01_circle',
        3: 'tasks.02_operations',
        4: 'tasks.03_favorite_movies',
        5: 'tasks.04_my_family',
        6: 'tasks.05_zoo',
        7: 'tasks.06_songs_list',
        8: 'tasks.07_secret',
        9: 'tasks.08_garden',
        10: 'tasks.09_shopping',
        11: 'tasks.10_store'
    }

    while True:
        print("\n Выберите задачу (1-11) или введите 0 для выхода:")
        for i in range(1, len(tasks) + 1):
            task_name = tasks[i].split('.')[-1]
            print(f"{i}: Задание {i} {task_name}")
        try:
            choice = int(input("Ваш выбор: "))
            
            if choice == 0:
                print("Выход из программы.")
                break
            elif choice in tasks:
                module_name = tasks[choice]
                module = importlib.import_module(module_name)
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число от 0 до 11.")
            
if __name__ == "__main__":
    main()
