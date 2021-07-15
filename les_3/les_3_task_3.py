'''3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
'''


print('Перестановка максимального и минимального элементов \
случайного массива.')

try:
    n = int(input('Введите число элементов случайного массива: \n'))
    if n <= 0:
        raise ValueError
    a, b = map(int, input('Введите нижнюю и верхнюю границы \
диапазона через пробел: \n').split(' '))

except ValueError:
    print('Неверный ввод.')
else:
    from random import randint
    rnd = [randint(a, b) for _ in range(n)]
    print('Массив случайных чисел: {}'.format(rnd))

    i_min, i_max = 0, 0
    for i, el in enumerate(rnd):
        if el < rnd[i_min]:
            i_min = i
        if el > rnd[i_max]:
            i_max = i

    rnd[i_max], rnd[i_min] = rnd[i_min], rnd[i_max]

    print('Результат: {}\n'.format(rnd))
