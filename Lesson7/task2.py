# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def rand_list_float_30():
    intro_list = [None] * random.randint(0, 30)
    for i in range(len(intro_list)):
        intro_list[i] = round(random.uniform(0, 50), 2)
    return intro_list

def insert_sort(intro_list):
    # O(n**2)
    print(intro_list)
    for i in range(1, len(intro_list)):
        key = intro_list[i]
        j = i - 1
        while intro_list[j] < key and j >= 0:
            intro_list[j + 1] = intro_list[j]
            j -= 1
        intro_list[j + 1] = key
    return intro_list

if __name__ == '__main__':
    print(insert_sort(rand_list_float_30()))




