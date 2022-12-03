# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# 67.82 -> 23
# (-0.56) -> 11

def get_int (float_):
    while round(float_, 9) % 10 != 0:
        float_ = round(float_, 9) * 10
    new_int = int(float_)
    return new_int // 10

def sum_of_digit(number):
    sum = 0 
    while number > 0:
        sum = sum + (number % 10)
        number = number // 10 
    return sum    

try:
    n = float(input('Введите вещественное число:\n'))
    num = abs(n)
    print(f'Число по модулю без запятой:{get_int(num)}')
    print(f'Сумма чисел:{sum_of_digit(get_int(num))}')
except ValueError:
    print("вы вели не число")