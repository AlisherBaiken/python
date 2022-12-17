#  Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#   В качестве символа-разделителя используйте пробел.
def find_max_min():
    input_string = input("введите число через пробел: ").split()
    input_string = list(map(int, input_string))
    print(f"max chislo: {max(input_string)}, min chislo {min(input_string)} ")

find_max_min()