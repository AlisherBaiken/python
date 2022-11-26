# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
print("Введите первое число: ")
a_number = int(input())
print("Введите второе число: ")
b_number = int(input())
print("Введите третье число: ")
c_number = int(input())
print("Введите четвертое число: ")
d_number = int(input())
print("Введите пятое число: ")
f_number = int(input())
max_number = 0
if b_number > a_number:
    max_number = b_number
if c_number > max_number:
    max_number = c_number
if d_number > max_number:
    max_number = d_number
if f_number > max_number:
    max_number = f_number
print(max_number)

# nums = [4, 6, 8, 22, 77, 2]
# maximum = nums[0]
# for i in nums:
# if maximum < i:
# maximum = i
# print (maximum)