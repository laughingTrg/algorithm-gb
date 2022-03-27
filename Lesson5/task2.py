

def sum_mul_hex(num1, num2):
    number1 = list(num1.upper())
    number2 = list(num2.upper())
    sum_hex = int(num1, 16) + int(num2, 16)
    mul_hex = int(num1, 16) * int(num2, 16)
    print(f'Summ of {number1} and {number2} =', list(hex(sum_hex).upper())[2:])
    print(f'Multiplication of {number1} and {number2} =', list(hex(mul_hex).upper())[2:])

if __name__ == '__main__':
    sum_mul_hex(input('Enter first hex number: '),
                input('Enter second hex number: '))

