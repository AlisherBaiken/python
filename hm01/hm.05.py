# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21
print("Введите через пробел координаты первой точки: ")
x_number, y_number = map(int,input().split(' '))
print("Введите через пробел координаты второй точки: ")
x_number2, y_number2 = map(int,input().split(' '))
distnace = float(((x_number2 - x_number)**2 + (y_number2 - y_number)**2)**0.5)
print(int(distnace * 100)/100)