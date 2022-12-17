# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
from typing import List


def show_el(lst: list) -> list:
    lst_new = []
    for i in lst:
        if i not in lst_new:
            lst_new.append(i)
    return lst_new
lst =list(input("Введите элементы через пробелы:\n ").split())

try:
    lst_of_number = list(map(int, lst))
    print(show_el(lst_of_number))

except ValueError:
    print(show_el(lst))