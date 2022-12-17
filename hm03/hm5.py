# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

from function import give_int


def fibo_pos(number: int) -> list:
    n_fibo = [0]
    fibo1 = 0
    fibo2 = 1
    neg = 1
    for i in range(1, number + 1):
        fibo1, fibo2 = fibo2, fibo1 + fibo2
        n_fibo.insert(0, neg * fibo1)
        neg *= -1
    return n_fibo

num = give_int("type number: ",1)
print(fibo_pos(num))

