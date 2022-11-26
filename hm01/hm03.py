# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x_number = int(input("Введите координату х:\n"))
y_number = int(input("Введите координату y:\n"))

if x_number > 0 and y_number > 0:
    print("1")
elif x_number < 0 and y_number < 0:
    print("2")
elif x_number < 0 and y_number > 0:
    print("3")
elif x_number > 0 and y_number < 0:
    print("4")
elif x_number == 0 and y_number == 0:
    print("Точка является началом")
elif x_number == 0:
    print("на оси Х")
elif y_number == 0:
    print("на оси У")     