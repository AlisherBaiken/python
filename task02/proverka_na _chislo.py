week_day = input("Ввудите день недели: ")
try: 
    week_day = int(week_day)
    print("Получилось")
except ValueError:
    print("Вы ввели не число")  

# kak funkcia
# def in_int(num):
#     try:
#         num = int(num)
#         return num
#     except ValueError:
#         return False

# kak rekursia
# def give_int(input_string):
#     try:
#         num = int(input(input_string))
#         return num
#     except :
#         return give_int(input_string)


