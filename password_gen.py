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
    if input_check_text(input('Добавить цифры? (да/нет, по умолчанию да): ')):
        random_base += string.digits
    if input_check_text(input('Добавить спецсимволы "%$#@!" ? (да/нет, по умолчанию да): ')):
        random_base += "%$#@!"
    if input_check_text(input('Исключить неопределенные символы "Ilo0O" ? (да/нет, по умолчанию да): ')):
        random_base = [symbol for symbol in random_base if symbol not in 'Ilo0O']
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
        # формирование базы для генерации паролей
        random_base = creating_random_base()

        print('\nСгенерированные пароли:')

        # формирование и отображение списка заданного количества паролей заданной длины
        generated_pass = [''.join(random.choices(random_base, k=len_pas)) for _ in range(count_pas)]
        print(*generated_pass, sep='\n')

        #запрос на новую генерацию пароля
        if input_check_text(input('\nХотите сгенерировать пароль ещё раз? (да/нет): ')):
            continue
        else:
            break
    escape = input('Нажмите ENTER для выхода')
main()