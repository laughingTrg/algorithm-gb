# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def math_operations():
    while True:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        sign = input('Enter operation sign or 0 ot exit: ')
        while True:
            if sign == '+' or sign == '-' or sign == '*' or sign == '/' or sign == '0':
                break
            sign = input('Please. Enter right operation sign (-, +, *, /) or 0 ot exit: ')
        if sign == '0':
            return print('Exit from program')
        if sign == '/' and num2 == 0:
            print('You know, that you can not to divide on 0.')
            while True:
                sign = input('Please. Enter right operation sign (-, +, *): ')
                if sign == '+' or sign == '-' or sign == '*':
                    break
        if sign == '-':
            print(f'{num1} - {num2} =', num1 - num2)
        elif sign == '+':
            print(f'{num1} + {num2} =', num1 + num2)
        elif sign == '*':
            print(f'{num1} * {num2} =', num1 * num2)
        else:
            print(f'{num1} / {num2} =', num1 / num2)
        print()


if __name__ == '__main__':
    math_operations()

