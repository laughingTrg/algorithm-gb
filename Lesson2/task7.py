# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

def natur_numbers(n):
    if n == 1:
        return 1
    return n + natur_numbers(n - 1)


if __name__ == '__main__':
    print(natur_numbers(int(input('Enter natural number: '))))



