# Написать программу, которая генерирует в указанных пользователем границах:
#   случайное целое число;
#   случайное вещественное число;
#   случайный символ.
import random

def get_random(start, end):
    if start.isdigit() and end.isdigit():
        print('Your random integer number:', end=' ')
        return print(random.randint(int(start), int(end)))
    elif '.' in start or '.' in end:
        print('Your random float number:', end=' ')
        return print(random.uniform(float(start), float(end)))
    else:
        print('Your random character:', end=' ')
        return print(chr(random.randint(ord(start), ord(end))))

if __name__ == '__main__':
    get_random(input('start: '),
               input('end: '))