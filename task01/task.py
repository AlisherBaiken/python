# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

first_number = int(input("Введите первое число:\n "))
second_number = int(input("Введите  второе число:\n "))

if first_number * first_number == second_number or second_number * second_number == first_number:
    print("ДА")
else:
    print("НЕТ")    
