'''7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба минимальны),
так и различаться.
'''


print('Определение двух наименьших элементов в массиве целых \
чисел')

try:
    n = int(input('Введите число элементов случайного массива: \n'))
    if n <= 0:
        raise ValueError
    a, b = map(int, input('Введите нижнюю и верхнюю границы \
диапазона через пробел: \n').split(' '))
    if a > b:
        a, b = b, a

except ValueError:
    print('Неверный ввод.')
else:
    from random import randint
    #the length of the random array is greater than the number of valid values
    rnd = [randint(a, b) for _ in range(2*(b-a+1))]
    print('Массив случайных чисел: {}'.format(rnd))

    min0, min1 = rnd[0], rnd[1]
    for el in rnd:
        if el <= min0 or el <= min1:
            if min0 <= min1:
                min1 = el
            else:
                min0 = el

    print('Два минимальных элемента: {} {}\n'.format(min0, min1))
