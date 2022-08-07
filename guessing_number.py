import random
from math import ceil, log2, floor

print('Привет! Давай сыграем в игру "Угадай число".\nТебе необходимо угадать целое число от 1 до 100.')


def is_valid(num: str) -> bool:
    '''
    Проверка корректности вводимых данных
    :param num:
    :return:
    '''
    return num.isdigit() and 0 < int(num) < 101 and float(num) % 1 == 0.0

def new_game(wish: str) -> bool:
    '''
    Запрос на запуск новой игры
    :param wish:
    :return:
    '''
    if wish in ['y', 'n']:
        return wish == 'y'
    else:
        wish = input('Неизвестная команда. Так вы хотите сыграть снова? (y - да, n - нет): ')
        return new_game(wish)


def game():
    number = random.randint(1, 100)
    attempt = input('Итак, игра началась! Введи предполагаемое число: ')
    count_try = 1
    while True:
        if not is_valid(attempt):
            attempt = input('Неверные данные. Введи целое число от 1 до 100: ')
            count_try += 1
            continue
        elif int(attempt) > number:
            attempt = input('Введенное число немного МЕНЬШЕ твоего. Попробуй снова: ')
            count_try += 1
            continue
        elif int(attempt) < number:
            attempt = input('Введенное число немного БОЛЬШЕ твоего. Попробуй снова: ')
            count_try += 1
            continue
        else:
            print(f'\nПоздравляю! Ты угадал число {attempt} с {count_try} попытки')
            break
    desire = input('\nОтличная игра! Хотите сыграть ещё раз? (y - да, n - нет): ')
    if new_game(desire):
        game()
    else:
        escape = input('\nСпасибо за игру! Ещё увидимся!\nНажмите Enter для выхода')

game()