# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def summ_of_digits (number):
    if 100 <= number <= 999:
        return print('Summ of digits of number is', int(str(number)[0]) + int(str(number)[1]) + int(str(number)[2]))
    return print("Your number does not have three digits")

def multi_of_digits (number):
    if 100 <= number <= 999:
        return print('Multiplication of digits of number is', int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2]))
    return print("Your number does not have three digits")


if __name__ == '__main__':
    number = int(input())
    summ_of_digits(number)
    multi_of_digits(number)


