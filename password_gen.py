import random
import string

print('Генератор безопасных паролей\n')

def input_digit_check(user_input_num: str) -> int:
    '''
    Проверка корректности вводимого числа
    :param user_input_num:
    :return:
    '''
    if user_input_num.isdigit() and float(user_input_num) % 1 == 0:
        return int(user_input_num)
    else:
        return input_digit_check(input('Ошибка ввода. Введите целое число: '))

def input_check_text(user_input_text = 'да') -> bool:
    '''
    Проверка корректности вводимого текста
    :param user_input_text:
    :return:
    '''
    if user_input_text in ['да', 'нет']:
        return user_input_text == 'да'
    else:
        return input_check_text(input('Ошибка ввода. Введите "да" или "нет": '))

def creating_random_base() -> str:
    '''
    Формирование базы символов для генерации пароля на основе пользовательских данных
    :return:
    '''
    random_base = string.ascii_letters
    if input_check_text(input('Включать цифры? (да/нет, по умолчанию да): ')):
        random_base += string.digits
    if input_check_text(input('Включать спецсимволы "%$#@!" ? (да/нет, по умолчанию да): ')):
        random_base += "%$#@!"
    if input_check_text(input('Исключать неопределенные символы "Ilo0O" ? (да/нет, по умолчанию да): ')):
        for symbol in "Ilo0O":
            if symbol in random_base:
                random_base = random_base.replace(symbol, '')
    return random_base

def main():
    '''
    Основная программа
    :return:
    '''
    while True:
        # считывание данных, вводимых пользователем
        count_pas = input_digit_check(input('Укажите количество паролей: '))
        len_pas = input_digit_check(input('Укажите длину одного пароля: '))
        # add_digits = input_check_text(input('Включать цифры? (да/нет): '))
        # add_punct = input_check_text(input('Включать спецсимволы "%$#@!" ? (да/нет): '))
        # exclude_uncertain = input_check_text(input('Исключать неопределенные символы "Ilo0O" ? (да/нет): '))
        # формирование базы для генерации паролей
        random_base = creating_random_base()

        print('\nСгенерированные пароли:')

        for _ in range(count_pas):
            for symbol in random.choices(random_base, k=len_pas):
                print(symbol, end='')
            print()

        if input_check_text(input('\nХотите сгенерировать пароль ещё раз? (да/нет): ')):
            continue
        else:
            break
    escape = input('Нажмите ENTER для выхода')

main()