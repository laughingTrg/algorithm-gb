# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


def summ_of_elements(list_numbers):
    return sum(list_numbers[list_numbers.index(min(list_numbers))+1: list_numbers.index(max(list_numbers))])

if __name__ == '__main__':
    list_numbers = [3, 2, 3, 5, 6, 7, 8, 3, 4, 5, 67, 5, 4, 23, 4, 5, 67, 5, 3, 23, 3]
    print(summ_of_elements(list_numbers))


