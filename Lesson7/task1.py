# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

def rand_list_30():
    list = [None] * random.randint(0, 30)
    for i in range(len(list)):
        list[i] = random.randint(-100, 100)
    return list

def bubble_sort(intro_list):
    # O(n**2)
    swapped = False
    for i in range(len(intro_list) - 1, 0, -1):
        for j in range(i):
            if intro_list[j] < intro_list[j + 1]:
                intro_list[j], intro_list[j + 1] = intro_list[j + 1], intro_list[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return intro_list

if __name__ == '__main__':
    print(bubble_sort(rand_list_30()))


