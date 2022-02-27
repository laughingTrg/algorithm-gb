# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

def summ_bits (num1, num2):
    return print("Summ of two numbers:", (num1 | num2))

def multi_bits (num1, num2):
    return print('Multiplication of two numbers:', (num1 & num2))

def xor_bits(num1, num2):
    return print('XOR of two numbers:', (num1 ^ num2))

def right_2_bits (number):
    return print('Swipe two bits to the right of number:', (number>>2))

def left_2_bits (number):
    return print('Swipe two bits to the left of number:', (number<<2))

if __name__ == '__main__':
    num1 = 5
    num2 = 6
    summ_bits(num1, num2)
    multi_bits(num1, num2)
    xor_bits(num1, num2)
    right_2_bits(num1) # сдвигаем число 0b101 вправо получается 0b001, что в десятичном виде равно 1
    left_2_bits(num1) # сдвигаем число 0b101 влево получаем 0b10100, что в десятичном виде равно 20



