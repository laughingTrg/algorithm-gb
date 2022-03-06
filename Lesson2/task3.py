# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def mirror_number(number):
    if len(number) == 1:
        return number
    return str(number[-1]) + mirror_number(number[:-1])

if __name__ == '__main__':
    print(mirror_number(input('Enter number to mirror: ')))