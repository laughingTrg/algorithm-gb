# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

def swipe_min_max():
    numbers = []
    idx_min = 0
    idx_max = 0
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
    return numbers

if __name__ == '__main__':
    print(swipe_min_max())

