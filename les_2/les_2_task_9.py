'''9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его
цифр.
'''


from functools import reduce

print('Поиск наибольшего натурального числа по сумме цифр.')
try:
    print('Введите последовательность чисел через пробел:')
    series = map(int, input().split(' '))

    max_number, max_res = 0, 0
    for number in series:
        res = int(reduce(lambda x, y: int(x) + int(y), str(number)))
        if not res:
            raise ValueError

        if res > max_res:
            max_number, max_res = number, res

    print(f'Искомое число: {max_number}, Сумма цифр: {max_res}')

except ValueError:
    print('Некорректный ввод')
