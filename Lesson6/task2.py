# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Разрядность ОС 64 бита Python версии 3.8
# Эта программа по памяти более эффективна, хотя массив жестко не задан размером

import sys

def idx_even_nums(numbers):
    res_list = []
    # print(sys.getsizeof(res_list), 'res_list') - под список выделено 56 байт
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            res_list.append(i)
    # print(sys.getsizeof(res_list), 'res_list') - под список со значениями выделено 88 байт
    return res_list

if __name__ == '__main__':
    numbers = [8, 3, 15, 6, 4, 2]
    # print(sys.getsizeof(numbers), 'numbers') - под вводный список выделено 88 байт
    print(idx_even_nums(numbers))

