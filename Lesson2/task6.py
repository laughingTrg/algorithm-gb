# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

def number_game():
    target = random.randint(0, 100)
    lives = 10
    while lives > 0:
        choice = int(input('Please enter a number to guess the target: '))
        if choice == target:
            return print(f'---You are winner. The target number is {target}---')
        elif choice > target:
            print(f'Target is less than {choice}')
            lives -= 1
        else:
            print(f'Target is more than {choice}')
            lives -= 1
    print(f'---You are looser. The target number is {target}---')


def number_game_rec(target, lives):
    choice = int(input('Please enter a number to guess the target: '))
    if choice == target and lives > 0:
        return print(f'---You are winner. The target number is {target}---')
    elif lives == 0:
        return print(f'---You are looser. The target number is {target}---')

    if choice > target:
        print(f'Target is less than {choice}')
        return number_game_rec(target, lives - 1)
    else:
        print(f'Target is more than {choice}')
        return number_game_rec(target, lives - 1)



if __name__ == "__main__":
    number_game()
    number_game_rec(random.randint(0, 100), 10)


