# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def odd_even_digit(number):
    odd_count = 0
    even_count = 0
    for i in number:
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return print(f'The number {number} has {even_count} even digits and {odd_count} odd digits.')

if __name__ == '__main__':
    odd_even_digit(input('Enter number: '))