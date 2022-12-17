# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from function import give_int, random_list

def summary_on_post(datalist):
    sum = 0
    for i in range(1,len(datalist),2):
        sum += datalist[i]
    return sum

size = give_int('value',1)
number = random_list(size)
print(number)
print(f'summa :{summary_on_post(number)}')