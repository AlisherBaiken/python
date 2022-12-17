# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.
#  НОК - наименьшее общее кратное,
#  которое делится и на первое, и на второе число.
num_1 = int(input("Введите число: "))
num_2 = int(input("Введите число: "))
num_3 = 0
del_num = 0
nod = 0
while num_1 != 0:
    num_1, num_2 = (num_1 % num_2), (num_1)
nod = num_1 + num_2
del_num = (num_1 * num_2) // nod
print(del_num)
# def calculate_lcm(x, y):  # selecting the greater number
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while (True):
#         if ((greater % x == 0) and (greater % y == 0)):
#             lcm = greater
#         break
#         greater += 1
#         return lcm
