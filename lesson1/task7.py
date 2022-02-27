# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

def is_triangle(side1, side2, side3):
    sides = [int(side1), int(side2), int(side3)]
    sides.sort()
    if sides[-1] >= (sides[0] + sides[1]):
        return print('Triangle is can\'t to be created.')
    else:
        if sides.count(sides[0]) > 1 or sides.count(sides[1]) > 1 or sides.count(sides[2]) > 1:
            if sides.count(sides[0]) > 2:
                return print('You can create equilateral triangle') # равносторонний треугольник
            return print('You can create isosceles triangle')       # равнобедренный треугольник
        return print('You can create versatile triangle')           # разносторонний треугольник

if __name__ == '__main__':
    is_triangle(input('Enter the length of first side: '),
                input('Enter the length of second side: '),
                input('Enter the length of third side: '))


