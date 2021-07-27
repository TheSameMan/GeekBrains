'''9. Найти максимальный элемент среди минимальных элементов
столбцов матрицы.
'''


print('Максимальный элемент среди минимальных элементов столбцов \
матрицы.')

try:
    nr, nc = map(int, input('Введите число строк и столбцов через \
пробел: \n').split(' '))
    if nr <= 0 or nc <= 0:
        raise ValueError
    a, b = map(int, input('Введите нижнюю и верхнюю границы \
диапазона через пробел: \n').split(' '))
    if a > b:
        a, b = b, a

except ValueError:
    print('Неверный ввод.')
else:
    from random import uniform
    mat = [[round(uniform(a, b), 1) for _ in range(nc)] for _ in range(nr)]

    print('\nСгенерированная матрица:')
    for row in mat:
        print(*row)

    min_r = a
    for i in range(nc):
        min_c = b
        for j in range(nr):
            if mat[j][i] < min_c:
                min_c = mat[j][i]

        if min_c >= min_r:
            min_r = min_c

    print(f'\nРезультат: {min_r}')
