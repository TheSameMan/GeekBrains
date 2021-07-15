'''6. В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами. Сами минимальный и
максимальный элементы в сумму не включать.
'''


print('Сумма элементов между максимальным и минимальным \
элементами массива.')

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
    rnd = [2, 1, 3]
    print('Массив случайных чисел: {}'.format(rnd))

    sm = 0
    min_el, max_el = float('inf'), float('-inf')
    min_k, max_k = 0, 0
    for el in rnd:
        sm += el
        if el > max_el:
            max_el = el
            max_k = 0
        if el == max_el:
            max_k += 1

        if el < min_el:
            min_el = el
            min_k = 0
        if el == min_el:
            min_k += 1

    print(f'Результат: {sm-min_el*min_k-max_el*max_k}')
