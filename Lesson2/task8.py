# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def count_digit(digit, number):
    if len(number) == 1:
        if number == digit:
            return 1
        return 0
    if number[0] == digit:
        return 1 + count_digit(digit, number[1:])
    return 0 + count_digit(digit, number[1:])

if __name__ == '__main__':
    print(count_digit(input('Enter digit to count: '), input('Enter stock number: ')))


