# Лабораторная работа №1
## 00_distance
__Задание__: Составить словарь словарей расстояний между городами, координаты которых даны.

## Описание проделанной работы
По указанной в задании формуле, рассчитаны расстояния между городами и записаны как кортежи в объявленные переменные.
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
    'Paris' : {'Moscow' : moscow_paris, 'London' : london_paris}
}
```

## Результаты вычислений
![res](result_00.png)

## Список используемых источников
1. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
   
