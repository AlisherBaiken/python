# 3-Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from function import give_int, random_list_float

def max_min(datalist:list) -> float:
    min = 0.0
    max = 1.0 
    for i in range(len(daata)):
        part = round(datalis[i] % 1, 4)
    if part >= max:
        max = part
    if part <= min:
        min = part
print(max)
print(min)
sum = round(max - min, 4)
return sum

size = give_int('type number: ' ,1)
number = random_list_float(size)
print(number)
print(f"raznica:{max_min(number)}")