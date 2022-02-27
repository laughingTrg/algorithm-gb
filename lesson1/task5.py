# Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят и сколько между ними находится букв.


def char_places (chr1, chr2):
    alphabet = []
    for _ in range(97, 123):
        alphabet.append(chr(_))
    if ord(chr2) > ord(chr1):
        return print(f'Place of char {chr1} is {alphabet.index(chr1) + 1}, '
                 f'place of char {chr2} is {alphabet.index(chr2) + 1}, '
                 f'between this chars {alphabet.index(chr2) - alphabet.index(chr1) - 1} characters')
    return print(f'Place of char {chr1} is {alphabet.index(chr1) + 1}, '
                 f'place of char {chr2} is {alphabet.index(chr2) + 1}, '
                 f'between this chars {alphabet.index(chr1) - alphabet.index(chr2) - 1} characters')

if __name__ == '__main__':
    char_places(input("Enter first char: "),
                input('Enter second char: '))




