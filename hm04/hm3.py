# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

from functions import get_list_data
from typing import List


def elemets(lst: list, trigger_str: str) -> list[str]:

    for i in range(len(str)):
        if trigger_str in lst[i]:
            lst[i] = lst[i].upper()
    return lst


lst = get_list_data("hm04\students.txt")
print(elemets(lst, '5'))
with open('hm04\students.txt', 'w', encoding='utf-8') as data:
    for i in range(len(lst)):
        data.writelines(f'{list[i]}\n')
