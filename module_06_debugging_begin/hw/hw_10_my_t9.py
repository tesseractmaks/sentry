"""
Представьте что мы решаем задачу следующего вида.
У нас есть кнопочный телефон (например, знаменитая Нокиа 3310) и мы хотим,
чтобы пользователь мог проще отправлять SMS.

Мы реализуем свой собственный клавиатурный помощник.
Каждой цифре телефона соответствует набор букв:
2 - a ,b, c
3 - d, e, f
4 - g, h, i
5 - j, k, l
6 - m, n, o
7 - p, q, r, s
8 - t, u, v
9 - w, x, y, z

Пользователь нажимает на клавиши, например,  22736368
    после чего на экране печатается basement

Напишите функцию-помощник my_t9, которая на вход принимает цифровую
строку и возвращает list из слов английского языка,
которые можно получить из этой цифровой строки.

В качестве словаря английского языка можете использовать
содержимое файла /usr/share/dict/words

Ваше решение должно работать с алгоритмической сложностью O(N),
где N -- длина цифровой строки.
"""

from collections import Counter
import re
import itertools


all_words=Counter()
n2l={
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}


with open('text.txt','r') as fin:
    for line in fin:
         all_words.update([word.lower() for word in re.findall(r'\b\w+\b',line)])


def combos(*nums):
    t=[n2l[i] for i in nums]
    return tuple(''.join(t) for t in itertools.product(*(t)))


def my_t9(*nums):
    combo=combos(*nums)
    c1=combos(nums[0])
    first_cut=(word for word in all_words if word.startswith(c1))
    res = (word for word in first_cut if word.startswith(combo))
    print(list(res))


if __name__ == "__main__":
    my_t9(7, 2)
