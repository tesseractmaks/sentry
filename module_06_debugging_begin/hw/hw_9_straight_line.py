"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""
from typing import List, Tuple


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    x_1, x_2, x_3, y_1, y_2, y_3 = list(*coordinates)
    if ((x_3 - x_1) / (x_2 - x_1) == (y_3 - y_1) / (y_2 - y_1)):
        print('лежат')
    else:
        print('не лежат')


if __name__ == '__main__':
    user_numbers = input()
    coordinates = []
    coordinates.append(map(float, list(user_numbers)))
    check_is_straight_line(coordinates)
