# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)
name_of_quarter = int(input("Введите номер четверти:\n"))
if name_of_quarter not in range(1,5):
    print("Введите число в диапозоне от 1 до 4")
elif name_of_quarter == 1:
    print("x∈(0, ∞) u y∈(0,∞)")
elif name_of_quarter == 2:
    print("x∈(0, -∞) u y∈(0,∞)")
elif name_of_quarter == 3:
    print("x∈(0, -∞) u y∈(0,-∞)")
else:
    print("x∈(0, ∞) u y∈(0,-∞)")
