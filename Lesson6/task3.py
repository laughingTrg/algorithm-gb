# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Разрядность ОС 64 бита Python версии 3.8

import random
import sys

def swipe_min_max():
    numbers = []
    # print(sys.getsizeof(numbers), 'numbers') - размер пустого списка 56 байт
    idx_min = 0
    # print(sys.getsizeof(idx_min), 'idx_min') - размер переменной 24 байта
    idx_max = 0
    # print(sys.getsizeof(idx_max), 'idx_max') - размер переменной 24 байта
    for i in range(20):
        numbers.append(random.randint(0, 100))
    for idx in range(len(numbers)):
        if numbers[idx] < numbers[idx_min]:
            idx_min = idx
        elif numbers[idx] > numbers[idx_max]:
            idx_max = idx
    min = numbers[idx_min]
    max = numbers[idx_max]
    numbers[idx_min] = max
    numbers[idx_max] = min
    # print(sys.getsizeof(numbers), 'numbers') - размер выводимого списка 256 Байт
    return numbers

if __name__ == '__main__':
    print(swipe_min_max())

