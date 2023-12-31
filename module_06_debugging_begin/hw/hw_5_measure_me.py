"""
Обычно мы пишем логи с какой-то целью.
Иногда для дебага, иногда для своевременного реагирования на ошибки.
Однако с логами можно делать очень-очень много чего.

Например, ведь верно, что каждая строка лога содержит в себе метку времени.
Таким образом, правильно организовав логгирование,
    мы можем вести статистику -- какая функция сколько времени выполняется.
Программа, которую вы видите в файле hw_5_measure_me.py пишет логи в stdout.
Внутри неё есть функция measure_me,
в начале и конце которой пишется "Enter measure_me" и "Leave measure_me".
Из-за конфигурации - в начале каждой строки с логами указано текущее время.
Запустите эту программу, соберите логи и посчитайте
среднее время выполнения функции measure_me.
"""
import datetime
import logging
import os
import random
import re

from typing import List

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.debug("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                            f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1
    logger.debug("Leave measure_me")
    return results


def get_average_time_run():
    with open("logs_hw_5.log", encoding="utf-8") as file:
        split_file = file.read().split("\n")
    time_start = re.split("[A-Za-z]", split_file[0])[0]
    time_end = re.split("[A-Za-z]", split_file[-2])[0]
    time_object_start = datetime.datetime.strptime(time_start.strip(), "%Y-%m-%d %H:%M:%S,%f")
    time_object_end = datetime.datetime.strptime(time_end.strip(), "%Y-%m-%d %H:%M:%S,%f")
    average_time_run = (time_object_end - time_object_start).seconds // 2
    print(f"Cреднее время выполнения функции measure_me: {average_time_run} секунд.")
    os.remove("./logs_hw_5.log")


if __name__ == "__main__":
    logging.basicConfig(
        level="DEBUG",
        filename="logs_hw_5.log",
        format="%(asctime)s %(message)s",
        filemode="a",
    )
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)
    get_average_time_run()
