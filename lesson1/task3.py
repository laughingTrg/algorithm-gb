#По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

def equation_of_line (x1, y1, x2, y2):
    k = round((y2 - y1)/(x2 - x1), 2)
    b = round((y1 - k * x1), 2)
    if b < 0:
        return print(f'The equation of line: y = {k}x - {abs(b)}')
    return print(f'The equation of line: y = {k}x + {b}')

if __name__ == '__main__':
    print('Please enter coordinates of two points')
    equation_of_line(float(input("x1 = ")),
                     float(input("y1 = ")),
                     float(input("x2 = ")),
                     float(input("y2 = ")))