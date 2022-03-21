"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os

ls_output_path = os.path.abspath("output_dir_avg.txt")


def get_mean_size(ls_output_path):
    with open(ls_output_path) as file:
        memory = [lines.split()[4] for lines in file.readlines()[1:]]
        memory_sum = sum(map(int, memory))
        print("Средний размер файла в папке:")
        print((memory_sum / len(memory) / 1024).__round__(2), 'мегабайт')


if __name__ == "__main__":
    get_mean_size(ls_output_path)
