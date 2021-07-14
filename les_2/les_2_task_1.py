'''1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не
завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в
качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '', '/'), программа должна сообщать об ошибке
и снова запрашивать знак операции. Также она должна сообщать
пользователю о невозможности деления на ноль, если он ввел его в
качестве делителя.
'''


print('Простой калькулятор для двух чисел.')
while True:
    try:
        a, b = map(float, input('Введите два числа:\n').split(' '))
    except ValueError:
        print('Ошибка: неверный ввод чисел')
        continue

    while True:
        print('Введите одну из операций:')
        op = str(input('+, -, *, / или 0, чтобы выйти:\n'))

        if op == '0':
            break

        if op not in ('+', '-', '*', '/', '0'):
            print('Ошибка: неверная операция')
            continue

        try:
            res = eval(f'{a} {op} {b}')
            print(f'{a} {op} {b} = {res}')
            break
        except ZeroDivisionError:
            print('Ошибка: деление на 0')
            continue

    if op == '0':
        break
