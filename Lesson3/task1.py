# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def divede_natur_number():
    div_numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    div_counts = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(2, 100):
        for num in div_numbers:
            if i % num == 0:
                div_counts[num - 2] += 1
    for num in div_numbers:
        print(f'In range from 2 to 99 count of numbers, which was diveded on {num}:', div_counts[num - 2])


if __name__ == '__main__':
    divede_natur_number()

