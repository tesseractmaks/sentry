"""
В своей работе программист должен часто уметь решать рутинные задачи.

Хорошим примером такой задачи является вычисление суммарного размера директории.

Пожалуйста реализуйте функцию, которая на вход принимает путь до папки
    в виде стрки или объекта Path
и возвращает суммарный объём директории в байтах.

В случае, если на вход функции передаётся несуществующий путь или НЕ директория,
    функция должна выкинуть исключение ValueError с красивым описание ошибки
"""

from pathlib import Path
from typing import Union


def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
    path = Path(directory_path)
    if Path.is_dir(path):

        size_in_bites = sum(files.stat().st_size for files in path.glob('**/*') if files.is_file())
        print(f"Size directory: {size_in_bites} bites")
    else:
        raise ValueError(
            f"Error the argument --{directory_path}-- is not a path or directory "
        )


calculate_directory_size()