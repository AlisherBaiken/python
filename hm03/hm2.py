# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from function import give_int, random_list

def pair_mult(datalist):
    multiple = list()
    for  i in range(len(datalist) // 2 + len(datalist) % 2):
        multiple.append(datalist[i] * datalist[-1-i])
    return multiple

size = give_int('value',1)
number = random_list(size)
print(number)
print(f"Pair is {pair_mult(number)}")