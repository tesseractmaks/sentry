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
import logging

import numpy as np

from typing import List


def get_average_salary_corrected(salaries: List[int]) -> float:
    logger.info(f"len salaries -  {len(salaries)}")
    logger.debug(f"len salaries - {len(salaries)}")
    logger.info(f"max salaries -  {max(array_salaries)}")
    logger.debug(f"min salaries - {min(array_salaries)}")
    salaries.remove(max(array_salaries)), salaries.remove(min(array_salaries))
    logger.info("max/min salaries - deleted")
    logger.debug("max/min salaries - deleted")
    avg_salaries = round(sum(salaries) / len(salaries), 2)
    logger.info(f"avg_salaries - {avg_salaries}")
    logger.debug("End program!")
    return avg_salaries


if __name__ == "__main__":
    logger = logging.getLogger("check")

    logging.basicConfig(
        level=logging.DEBUG, filename='logs.log',
        format='%(levelname)s --- %(name)s - %(asctime)s %(message)s',
        filemode="w"
    )

    n = 60
    start = 20000
    end = 30000
    array_salaries = np.random.uniform(low=start, high=end, size=(n,))

    logger.debug("Start program!")
    logger.debug(f"O(N) = {n}")

    print(get_average_salary_corrected(list(array_salaries)))
