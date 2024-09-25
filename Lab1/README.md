# Лабораторная работа 1
## Список заданий:
1. **`00_distance.py`**
   - **Задача:** Составим словарь словарей расстояний между ними
   - **Реализация:**
     ```python
     moscow = sites['Moscow']
     london = sites['London']
     paris = sites['Paris']

     moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1]-london[1]) ** 2) ** 0.5
     moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1]-paris[1]) ** 2) ** 0.5
     london_paris = ((london[0] - paris[0]) ** 2 + (london[1]-paris[1]) ** 2) ** 0.5

     distances = {
        'Moscow' : {'London' : moscow_london, 'Paris' : moscow_paris},
        'London' : {'Moscow' : moscow_london, 'Paris' : london_paris},
        'Paris' : {'Moscow' : moscow_paris, 'London' :  london_paris}
     }

     pprint(distances)
     ```

2. **`01_circle.py`**
   - **Задача:** 
     - Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
     - Если точка point лежит внутри того самого круга, то выведите на консоль True, Или False, если точка лежит вовне круга.
     - Аналогично для другой точки
   - **Реализация:**
     ```python
     square = round(radius ** 2 * 3.1415926, 4)
     print(square)
     distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
     if distance_1 <= radius: 
         print('True')
     else:
         print('False')

     distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
     if distance_2 <= radius: 
         print('True')
     else:
         print('False')
     ```

3. **`02_operations.py`**
   - **Задача:** Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25"
   - **Реализация:**
     ```python
     result = 1 * (2 + 3) + (4 * 5)
     print(result)
     ```

4. **`03_my_favorite_movies.py`**
   - **Задача:** 
     - Выведите на консоль с помощью индексации строки, последовательно:
       - первый фильм 
       - последний 
       - второй 
       - второй с конца
   - **Реализация:**
     ```python
     print("Первый фильм - " + my_favorite_movies[0 : 10])

     print("Последний фильм - " + my_favorite_movies[42 : 57])

     print("Второй фильм - " + my_favorite_movies[12 : 25])

     print("Второй с конца фильм - " + my_favorite_movies[35 : 40])
     ```

5. **`04_my_family.py`**
   - **Задача:** 
     - Выведите на консоль рост отца в формате "Рост отца - ХХ см"
     - Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
   - **Реализация:**
     ```python
     my_family_height = [
        ['Марина', 172],
        ['Роман', 177],
        ['Валерий', 176]
     ]
     height_father = my_family_height[2][1]
     print('Рост отца -', height_father, 'см')
     ```

1. **`05_zoo.py`**
   - **Задача:** 
     - Посадите медведя (bear) между львом и кенгуру
     - Добавьте птиц из списка birds в последние клетки зоопарка
     - Уберите слона
     - Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
   - **Реализация:**
     ```python
     zoo.insert(1,'bear')
     print(zoo)

     birds = ['rooster', 'ostrich', 'lark', ]

     zoo.extend(birds)
     print(zoo)

     zoo.remove('elephant')
     print(zoo)

     print('Лев сидит в', zoo.index('lion') + 1, 'клетке,', 'a жаворонок сидит в', zoo.index('lark') + 1, 'клетке.')
     ```

2. **`06_songs_list.py`**
   - **Задача:** 
     - Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате.
     - Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
   - **Реализация:**
     ```python
      halo_enjoy_clean = round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1], 2)

      print('Три песни звучат', halo_enjoy_clean, 'минут')

      sweetest_policy_blue = round(violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth']
                             + violator_songs_dict['Blue Dress'])
    
     print('А другие три песни звучат', sweetest_policy_blue, 'минут')
     ```

3. **`07_secret.py`**
   - **Задача:** Расшифровать заданный шифр следую подсказкам.
   - **Реализация:**
     ```python
     first = secret_message[0][3]
     second = secret_message[1][9 : 13]
     third = secret_message[2][5 : 15: 2]
     fourth = secret_message[3][12 : 6 : -1]
     fifth = secret_message[4][20:15:-1]
     print(first, second, third, fourth, fifth)
     ```

4. **`08_garden.py`**
   - **Задача:** 
     - Создайте множество цветов, произрастающих в саду и на лугу
     - Выведите на консоль все виды цветов
     - Выведите на консоль те, которые растут и там и там
     - Выведите на консоль те, которые растут в саду, но не растут на лугу
     - Выведите на консоль те, которые растут на лугу, но не растут в саду
   - **Реализация:**
     ```python
     garden_set = set(garden)
     meadow_set = set(meadow)
    
     # выведите на консоль все виды цветов
     print(garden_set | meadow_set)

     # выведите на консоль те, которые растут и там и там
     print(garden_set & meadow_set)

     # выведите на консоль те, которые растут в саду, но не растут на лугу
     print(garden_set - meadow_set)

     # выведите на консоль те, которые растут на лугу, но не растут в саду
     print(meadow_set - garden_set)
     ```
5.  **`09_shopping.py`**
    - **Задача:** Создайте словарь цен на продукты следующего вида (писать прямо в коде).
    - **Реализация:**
      ```python
      sweets = {
        'печенье': [
            {'shop': 'ашан', 'price': 10.99},
            {'shop': 'пятерочка', 'price': 9.99}
        ],
        'конфеты': [
            {'shop': 'пятерочка', 'price': 32.99},
            {'shop': 'магнит', 'price': 30.99},
        ],
        'карамель': [
            {'shop': 'ашан', 'price': 45.99},
            {'shop': 'магнит', 'price': 41.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ]
      }
      ```
     
6.  **`10_store.py`**
    - **Задача:** Вывести стоимость каждого вида товара на складе.
    - **Реализация:**
      ```python
      # Столы
      table_code = goods['Стол']
      table_item1 = store[table_code][0]
      table_item2 = store[table_code][1]
      table_quantity = table_item1['quantity'] + table_item2['quantity']
      table_price1 = table_item1['price']
      table_price2 = table_item2['price']
      table_cost = table_item1['quantity'] * table_price1 + table_item2['quantity'] * table_price2
      print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

      # Диваны
      sofa_code = goods['Диван']
      sofa_item1 = store[sofa_code][0]
      sofa_item2 = store[sofa_code][1]
      sofa_quantity = sofa_item1['quantity'] + sofa_item2['quantity']
      sofa_price1 = sofa_item1['price']
      sofa_price2 = sofa_item2['price']
      sofa_cost = sofa_item1['quantity'] * sofa_price1 + sofa_item2['quantity'] * sofa_price2
      print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

      # Стулья
      chair_code = goods['Стул']
      chair_item1 = store[chair_code][0]
      chair_item2 = store[chair_code][1]
      chair_item3 = store[chair_code][2]
      chair_quantity = chair_item1['quantity'] + chair_item2['quantity'] + chair_item3['quantity']
      chair_price1 = chair_item1['price']
      chair_price2 = chair_item2['price']
      chair_price3 = chair_item3['price']
      chair_cost = chair_item1['quantity'] * chair_price1 + chair_item2['quantity'] * chair_price2 + chair_item3['quantity'] * chair_price3
      print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')
      ```

## Список используемых источников
1. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
   

   
