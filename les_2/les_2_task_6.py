'''6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или
меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
'''


from random import randint

print('Угадайте число от 0 до 100.')
rnd = randint(0, 100)
n = 10
while n > 0:
    print(f'Осталось {n} попыток.')
    try:
        ans = int(input())
    except ValueError:
        print('Некорректный ввод')
        continue

    if ans == rnd:
        print('Вы угадали!\n')
        break

    n -= 1
    if n == 0:
        print(f'Попытки закончились. Верный ответ {rnd}')
    else:
        print(f"""Загаданное число \
{'больше' if rnd > ans else 'меньше'}.""")