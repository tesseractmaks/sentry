"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
import random
from typing import List

import numpy as np


def get_average_salary_corrected(salaries: List[int]) -> float:

    # x= sorted(list(map(int, array_salaries)))
    # print(x)
    # print()
    #
    # cut_array_salaries = np.delete(np.sort(array_salaries), [[0], [-1]]),  # np.delete(array_salaries, [-1])
    #
    # print(np.count_nonzero(array_salaries))
    # print(np.count_nonzero(cut_array_salaries))
    # avg_salaries = np.sum(cut_array_salaries) / np.count_nonzero(cut_array_salaries)
    # print(int(avg_salaries))
    #
    #
    # n = 60
    #
    # array_salaries = random.choices(test_generate_array, k=n)
    # print()
    # x = sorted(list(map(int, array_salaries)))
    # print(x)
    print(sorted(salaries))
    print(len(salaries))
    salaries.remove(max(array_salaries)), salaries.remove(min(array_salaries))
    print(sorted(salaries))
    print(len(salaries))
    print()

    avg_salaries = sum(salaries) / len(salaries)
    print(round(avg_salaries, 2))
    return avg_salaries
#
# start= round(random.uniform(33, 66), 2)
# end = round(random.uniform(33, 66), 2)
# salaries_array = list(range(start, end))
#
# start = 20000
# end = 30000

# sampl = numpy.random.uniform(low=start, high=end, size=(50,))
# y=list(map(lambda i: i.round(2), sampl))

n = 60

start = 20000
end = 30000
# array_salaries = random.choices(test_generate_array, k=n)
array_salaries = np.random.uniform(low=start, high=end, size=(n,))
# print(sorted(array_salaries))

get_average_salary_corrected(list(array_salaries))