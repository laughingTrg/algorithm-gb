# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


def matrix_with_sum():
    input_data = input('Enter 16 elements of matrix with "," like delimiter : ')
    list_data = input_data.split(',')
    for i in range(len(list_data)):
        list_data[i] = int(list_data[i])
    for i in range(4):
        print(*list_data[i*4: 4+i*4], sum(list_data[i*4: 4+i*4]))


    return


if __name__ == '__main__':
    matrix_with_sum()

