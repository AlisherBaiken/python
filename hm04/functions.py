def give_int(input_string):
    try:
        num = int(input(input_string))
        return num
    except:
        return give_int(input_string)


def get_list_data(filename: str) -> List(str):
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')
