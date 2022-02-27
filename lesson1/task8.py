# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        return print(f'{year} - this year is leap')  # високосный год
    return print(f'{year} - this year is not leap') # не високосный год

if __name__ == '__main__':
    is_leap_year(int(input('Enter year: ')))





