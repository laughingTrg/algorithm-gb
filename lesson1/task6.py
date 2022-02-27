# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def what_is_char_en(num1):
    alphabet = []
    for _ in range(97, 123):
        alphabet.append(chr(_))
    return print(f'In english alphabet place {num1} of character {alphabet[int(num1) - 1]}')

def what_is_char_ru(num1):
    alphabet = []
    for _ in range(1072, 1104):
        alphabet.append(chr(_))
    return print(f'In russian alphabet place {num1} of character {alphabet[int(num1) - 1]}')

if __name__ == '__main__':
    what_is_char_en(input('Enter place of english char: '))
    what_is_char_ru(input('Enter place of russian char: '))






