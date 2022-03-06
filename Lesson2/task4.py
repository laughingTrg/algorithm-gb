# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def summ_of_elements(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return (-1 / 2**(n-1)) + summ_of_elements(n - 1)
    else:
        return (1 / 2**(n-1)) + summ_of_elements(n - 1)


if __name__ == '__main__':
    print(summ_of_elements(int(input('Enter count of elements: '))))



