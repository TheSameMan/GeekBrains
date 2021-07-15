'''5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''


print('Поиск максимального отрицательного элемента массива.')

try:
    n = int(input('Введите число элементов случайного массива: \n'))
    if n <= 0:
        raise ValueError
    a, b = map(float, input('Введите нижнюю и верхнюю границы \
диапазона через пробел: \n').split(' '))

except ValueError:
    print('Неверный ввод.')
else:
    from random import uniform
    rnd = [round(uniform(a, b), 3) for _ in range(n)]
    print('Массив случайных чисел: {}'.format(rnd))

    min_i, min_el = '-', '-'
    catched = False
    for i, el in enumerate(rnd):
        if el < 0:
            if not catched:
                min_i, min_el = i, el
                catched = True

            if el > min_el:
                min_i, min_el = i, el

    print(f'Максимальный отрицательный элемент: {min_el}, индекс: \
{min_i}')
