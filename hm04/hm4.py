# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
#  При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, 
# считывает текст и дешифровывает его.
import string
eng_abc = string.ascii_letters + string.ascii_lowercase + string.punctuation
rus_abc = 'абвгдеёжзийклмнопрстуфхчшщьъэюя' + string.punctuation
text = '''
Я к вам пишу — чего же боле?
Что я могу еще сказать?
Теперь, я знаю, в вашей воле
Меня презреньем наказать.
Но вы, к моей несчастной доле
Хоть каплю жалости храня,
Вы не оставите меня. 
'''
def crypt_text(text:str, key: int):
    new_text = ''
    for index, letter in enumerate(text):
        use_abc = rus_abc if letter in rus_abc else eng_abc
        letter_index = use_abc.find(letter)
        new_place = (letter_index + key) % len(rus_abc)
        if letter in rus_abc:
            new_text += use_abc[new_place]
        else:
            new_text += letter
    return new_text       

crypted_text = crypt_text(text, 3)
print(crypted_text)
decrypted_text = crypted_text(text, -3)
print(decrypted_text)
