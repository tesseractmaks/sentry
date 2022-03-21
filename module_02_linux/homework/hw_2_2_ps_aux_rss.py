"""
С помощью команды ps можно посмотреть список процессов, запущенных текущим пользователем.
Особенно эта команда выразительна с флагами
    $ ps aux
Запустите эту команду, output сохраните в файл, например вот так
$ ps aux > output_file.txt
В этом файле вы найдёте информацию обо всех процессах, запущенных в системе.
В частности там есть информация о потребляемой процессами памяти - это столбец RSS .
Напишите в функцию python, которая будет на вход принимать путь до файла с output
и на выход возвращать суммарный объём потребляемой памяти в человеко-читаемом формате.
Это означает, что ответ надо будет перевести в байты, килобайты, мегабайты и тд.

Для перевода можете воспользоваться функцией _sizeof_fmt
"""
import os


def _sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


path = os.path.abspath("output_file.txt")


def get_summary_rss(path):
    with open(path) as file:
        memory = [lines.split()[5] for lines in file.readlines()]
        memory_sum = sum(map(int, memory[1:]))
        print("Суммарный объём потребляемой памяти:")
        print(memory_sum * 1024, 'байт')
        print(memory_sum, 'килобайт')
        print((memory_sum / 1024).__round__(2), 'мегабайт')
        print((memory_sum / 1024 / 1024).__round__(2), 'гигабайт')


if __name__ == "__main__":
    get_summary_rss(path)


