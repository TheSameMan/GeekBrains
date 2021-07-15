'''4. Определить, какое число в массиве встречается чаще
всего.
'''


print('Определение самого частого числа в массиве.')

try:
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

    counts = {}
    for el in rnd:
        try:
            counts[el] += 1
        except KeyError:
            counts[el] = 1

    max_item = 0, 0
    for item in counts.items():
        if max_item[1] < item[1]:
            max_item = item

    print(f'Чаще всего встречается число {max_item[0]}. Частота \
встречаемости {max_item[1]}')
