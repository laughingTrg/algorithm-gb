# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def two_min_numbers(list_numbers):
    one_min = min(list_numbers)
    idx_one_min = list_numbers.index(one_min)
    two_min = min(list_numbers[:idx_one_min], list_numbers[idx_one_min + 1:])
    return print('One min element:', one_min, '\n', 'Two min element:', *two_min)

if __name__ == '__main__':
    list_numbers = [3, 2, 3, 5, 6, 7, 8, 3, 4, 5, 67, 5, 4, 23, 4, 5, 67, 5, 3, 23, 3]
    two_min_numbers(list_numbers)
