# Определить, какое число в массиве встречается чаще всего
# Разрядность ОС 64 бита Python версии 3.8
import sys

def often_number(numbers):
    often_num = 0
    count_often_num = 0
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) > count_often_num:
            often_num = numbers[i]
            count_often_num = numbers.count(numbers[i])
    # print(sys.getsizeof(often_num)) - под переменную выделено 28 байт памяти
    return often_num


if __name__ == '__main__':
    list_numbers = [3,2,3,5,6,7,8,3,4,5,67,5,4,23,4,5,67,5,3,23,3]
    # print(sys.getsizeof(list_numbers)) под переменную выделено 224 Байта памяти
    print(often_number(list_numbers))



