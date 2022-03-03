# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def summ_of_digits(number):
    if len(number) == 1:
        return int(number)

    return int(number[0]) + summ_of_digits(number[1:])

def compare_numbers(*args):
    numbers = args
    out_number = ''
    summ_digits = 0
    for i in numbers:
        if summ_of_digits(str(i)) > summ_digits:
            summ_digits = summ_of_digits(str(i))
            out_number = i
    return print(f'Max summ of digits {summ_digits} of number {out_number}')

if __name__ == '__main__':
    compare_numbers(12, 23, 35)




