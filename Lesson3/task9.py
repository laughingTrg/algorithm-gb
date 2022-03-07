# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def min_element_mx():
    input_data = input('Enter 16 elements of matrix with "," like delimiter : ')
    list_data = input_data.split(',')
    list_min_el = []
    for i in range(len(list_data)):
        list_data[i] = int(list_data[i])
    for i in range(4):
        list_min_el.append(min(list_data[i*4: 4+i*4]))
    return print(max(list_min_el))

if __name__ == '__main__':
    min_element_mx()



