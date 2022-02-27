# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def middle_number(num1, num2, num3):
    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        numbers = [int(num1), int(num2), int(num3)]
        numbers.sort()
        return print('Middle number is', numbers[1])
    numbers = [float(num1), float(num2), float(num3)]
    numbers.sort()
    return print('Middle number is', numbers[1])

if __name__ == '__main__':
    middle_number(input('Enter first number: '),
                  input('Enter second number: '),
                  input('Enter third number: '))