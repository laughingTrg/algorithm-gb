# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import time

# Сложность алгоритма оставляет О(n*log(log(n)))
def eratosphen_simple_num(num):
    num = int(num)
    limit_numbers = num * 10
    numbers = [0] * limit_numbers
    for i in range(limit_numbers):
        numbers[i] = i

    numbers[1] = 0
    idx = 2
    count_simple_num = 0
    while idx < limit_numbers:
        if numbers[idx] != 0:
            count_simple_num += 1
            if count_simple_num == num:
                return print(idx)
            inc_idx = idx * 2
            while inc_idx < limit_numbers:
                numbers[inc_idx] = 0
                inc_idx += idx
        idx += 1

# Мой алгоритм
# Сложность алгоритма составляет O(n**2), т.к. мы используем вложенный цикл.
def simple_nums(num):
    num = int(num)
    limit_numbers = num * 10
    if num == 1:
        return print(2)
    count_simple_num = 0
    for number in range(2, limit_numbers):
        sub_count = 0
        for sub in range(2, number):
            if number % sub == 0:
                sub_count += 1
        if sub_count == 0:
            count_simple_num += 1
        if count_simple_num == num:
            return print(number)



if __name__ == '__main__':
    start_time = time.time()
    eratosphen_simple_num(input('Enter serial number of simple numbers (Eratosphen\'s Algorithm): '))
    print('Time of work Eratosphen\'s Algorithm:', time.time() - start_time)
    print()
    start_time = time.time()
    simple_nums(input('Enter serial number of simple numbers (my Algorithm): '))
    print('Time of work my Algorithm:', time.time() - start_time)


