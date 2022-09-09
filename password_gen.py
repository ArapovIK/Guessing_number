import random
import string

print('Генератор безопасных паролей\n')

random_base = string.ascii_letters

count_pas = int(input('Укажите количество паролей: '))
len_pas = int(input('Укажите длину одного пароля: '))
add_digits = input('Включать цифры? (да/нет): ')
add_punct = input('Включать спецсимволы "%$#@!" ? (да/нет): ')
exclude_uncertain = input('Исключать неопределенные символы "Ilo0O" ? (да/нет): ')

if add_digits == 'да':
    random_base += string.digits
if add_punct == 'да':
    random_base += "%$#@!"
if exclude_uncertain == 'да':
    for symbol in "Ilo0O":
        if symbol in random_base:
            random_base = random_base.replace(symbol, '')


print('Сгенерированные пароли:')

for _ in range(count_pas):
    for symbol in random.choices(random_base, k=len_pas):
        print(symbol, end='')
    print()

escape = input('Нажмите ENTER для выхода')
