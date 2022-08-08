import random
from math import ceil, log2

print('Привет! Давай сыграем в игру "Угадай число".\n\nТебе необходимо угадать целое число в заданном диапазоне\
 за ограниченное количество попыток.\n')

def is_valid(low, high, num: str) -> bool:
    """
    Проверка корректности вводимых данных
    :param num:
    :return:
    """
    return num.isdigit() and low <= int(num) <= high and float(num) % 1 == 0.0

def is_valid_low_range(edge: str) -> int:
    """
    Проверка введенной нижней границы
    :param edge:
    :return:
    """
    if edge.isdigit():
        return int(edge)
    else:
        edge = input('Введено неверное значение нижней границы. Введите целое число: ')
        return is_valid_low_range(edge)

def is_valid_high_range(edge: str, low) -> int:
    """
    Проверка введенной верхней границы
    :param edge:
    :param low:
    :return:
    """
    if edge.isdigit() and int(edge) > low:
        return int(edge)
    else:
        edge = input('Введено неверное значение верхней границы. Введите целое число, первышающее нижнюю границу: ')
        return is_valid_high_range(edge, low)

def new_game(wish: str) -> bool:
    """
    Запрос на запуск новой игры
    :param wish:
    :return:
    """
    if wish in ['y', 'n']:
        return wish == 'y'
    else:
        wish = input('Неизвестная команда. Так вы хотите сыграть снова? (y - да, n - нет): ')
        return new_game(wish)


def game():
    while True:
        low_range = is_valid_low_range(input('Введите нижнюю границу диапазона: '))
        high_range = is_valid_high_range(input('Введите верхнюю границу диапазона: '), low_range)
        number = random.randint(low_range, high_range)      #выбор случайно числа из заданного диапазона
        try_limit = ceil(log2(high_range - low_range + 2))      #ограничение количества попыток
        # '+ 2' добавлено для определения минимального количества попыток, равного двум, для любого диапазона угадывания
        attempt = input(f'\nИтак, игра началась!\n\
Загадано число от {low_range} до {high_range}. Количество попыток: {try_limit}. Справишься? {chr(128520)}\n\
Введи предполагаемое число: ')

        for try_number in range(1, try_limit + 1):
            if not is_valid(low_range, high_range, attempt):
                attempt = input(f'Неверные данные. Введи целое число от {low_range} до {high_range}: ')
                continue
            elif int(attempt) == number:
                print(f'\nПоздравляю! Ты угадал число {attempt} с {try_number} попытки\nОтличная игра!')
                break
            elif int(attempt) > number:
                attempt = input(f'Загаданное число МЕНЬШЕ вашего. Осталось попыток: {try_limit - try_number}\n\
Попробуй снова: ')
                continue
            else:
                attempt = input(f'Загаданное число БОЛЬШЕ вашего. Осталось попыток: {try_limit - try_number}\n\
Попробуй снова: ')
                continue
        else:
            print('Упс, попытки закончились...')
        desire = input('\nХотите сыграть ещё раз? (y - да, n - нет): ')
        if new_game(desire):    #проверка результата запроса на новую игру
            continue
        else:
            break
    escape = input('\nСпасибо за игру! Ещё увидимся!\nНажмите Enter для выхода')

game()