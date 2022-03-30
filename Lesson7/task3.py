# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках
import random


def intro_list(count):
    intro_list = [None] * (2 * count + 1)
    for i in range(len(intro_list)):
        intro_list[i] = random.randint(0, 100)
    return intro_list

# Сложность алгоритма O(n**2)
def median_of_list(numbers):
    print(numbers)
    less_median_count = 0
    more_median_count = 0

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                less_median_count += 1
            elif numbers[i] < numbers[j]:
                more_median_count += 1
        if less_median_count == more_median_count:
            return numbers[i]
        else:
            less_median_count, more_median_count = 0, 0


if __name__ == '__main__':
    print(median_of_list(intro_list(int(input('Enter number of list where length of list (2m + 1): ')))))

