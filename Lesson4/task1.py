# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import timeit
import time

# Сложность алгоритма O(n) т.к. мы проходим по каждому элементу списка.
def max_negative(numbers):
    idx_neg_num = 0
    max_neg_num = -999999
    for i in range(len(numbers)):
        if numbers[i] < 0:
            if numbers[i] > max_neg_num:
                max_neg_num = numbers[i]
                idx_neg_num = i
    return (f'Max negative number in list: {max_neg_num} with index in list: {idx_neg_num}')


if __name__ == '__main__':
    list_numbers = [-3, -2, -3, 5,6,7,8,3,4,5, -67,5,4,-23,4,5,67,5,3,23,3]
    start_time = timeit.default_timer()
    print(max_negative(list_numbers))
    print('Time of the first algorithm is:', timeit.default_timer() - start_time)

# Модуль time почему-то выдает меньше времени на выполнение операции
    start_time = time.time()
    print(max_negative(list_numbers))
    print('Time of the first algorithm is:', time.time() - start_time)


