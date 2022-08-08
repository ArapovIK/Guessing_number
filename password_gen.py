import random

print('Генератор безопасных паролей')

digits = '12345567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count_pas = input('Укажите количество паролей: ')
len_pas = input('Укажите длину одного пароля: ')
add_digits = input('Включать цифры? (да/нет): ')
add_uppercase = input('Включать прописные буквы? (да/нет): ')
add_lowcase = input('Включать строчные буквы? (да/нет): ')
add_punct = input('Включать спецсимволы "!#$%&*+-=?@^_" ? (да/нет): ')
exclude_uncertain = input('Исключать неопределенные символы "il1Lo0O" ? (да/нет): ')


