# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# 45 -> 101101
# 3 -> 11
# 2 -> 10
from function import give_int
def int_to_binar(number:int)->str:
    binar = []
    while number //2 != 0:
        binar.insert(0, number % 2)
        number //= 2
    binar.insert(0,number)
    result = "".join(map(str,binar))
    return result

num = give_int("Enter number: ", 1)
binar = int_to_binar(num)
print(f"{num} = 0b{binar}")

