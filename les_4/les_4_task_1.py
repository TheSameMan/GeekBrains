'''1. Проанализировать скорость и сложность одного любого
алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с
кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''


#Профилирование кода для задачи:
#4. Определить, какое число в массиве встречается чаще всего.


if __name__ == '__main__':
    import cProfile
    from random import randint

    rnd = [randint(0, 10) for _ in range(1000)]
    print(rnd)

#Вариант 1
def freq_num1(a):
    counts = {}
    for el in a:
        try:
            counts[el] += 1
        except KeyError:
            counts[el] = 1

    max_item = 0, 0
    for item in counts.items():
        if max_item[1] < item[1]:
            max_item = item

    return max_item

#Вариант 2
def freq_num2(a):
    from collections import Counter
    return Counter(a).most_common(1)[0]

#Вариант 3
def freq_num3(a):
    num, max_freq = a[0], 1

    for i in range(len(a)-1):
        frq = 1
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                frq += 1

        if frq > max_freq:
            max_freq = frq
            num = a[i]

    return num, max_freq

if __name__ == '__main__':
    print(f'Вариант 1: {freq_num1(rnd)}')
    print(f'Вариант 2: {freq_num2(rnd)}')
    print(f'Вариант 3: {freq_num3(rnd)}')
# Все варианты совпадают

'''
Команды тестирования:
python -m timeit -n 100 -s "import les_4_task_1; from random import randint"
    "les_4_task_1.freq_num1([randint(0, 10) for _ in range(N)])"
python -m timeit -n 100 -s "import les_4_task_1; from random import randint"
    "les_4_task_1.freq_num2([randint(0, 10) for _ in range(N)])"
python -m timeit -n 100 -s "import les_4_task_1; from random import randint"
    "les_4_task_1.freq_num3([randint(0, 10) for _ in range(N)])"
'''

# N = 100
# Вариант 1: 100 loops, best of 5: 114 usec per loop
# Вариант 2: 100 loops, best of 5: 128 usec per loop
# Вариант 3: 100 loops, best of 5: 571 usec per loop

# N = 1000
# Вариант 1: 100 loops, best of 5: 1.15 msec per loop
# Вариант 2: 100 loops, best of 5: 1.14 msec per loop
# Вариант 3: 100 loops, best of 5: 51.1 msec per loop

# N = 10000
# Вариант 1: 100 loops, best of 5: 12.4 msec per loop
# Вариант 2: 100 loops, best of 5: 11.8 msec per loop
# Вариант 3: 100 loops, best of 5: 5.13 sec per loop

# Сложность алгоритмов 1 и 2 O(n), сложность варианта 3 - O(n^2).

if __name__ == '__main__':
    N = [100, 1000, 10000]
    for n in N:
        print(f'Вариант 1: N = {n}')
        cProfile.run('freq_num1([randint(0, 10) for _ in range(n)])')
        print(f'Вариант 2: N = {n}')
        cProfile.run('freq_num2([randint(0, 10) for _ in range(n)])')
        print(f'Вариант 3: N = {n}')
        cProfile.run('freq_num3([randint(0, 10) for _ in range(n)])')

# Вариант 1: N = 100
#          551 function calls in 0.001 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:29(freq_num1)

# Вариант 2: N = 100
#          586 function calls (574 primitive calls) in 0.001 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:45(freq_num2)

# Вариант 3: N = 100
#          639 function calls in 0.002 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.001    0.001 les_4_task_1.py:50(freq_num3)


# Вариант 1: N = 1000
#          5483 function calls in 0.005 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:29(freq_num1)

# Вариант 2: N = 1000
#          5491 function calls in 0.005 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:45(freq_num2)

# Вариант 3: N = 1000
#          6457 function calls in 0.099 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.091    0.091    0.091    0.091 les_4_task_1.py:50(freq_num3)


# Вариант 1: N = 10000
#          54618 function calls in 0.048 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.002    0.002 les_4_task_1.py:29(freq_num1)

# Вариант 2: N = 10000
#          54621 function calls in 0.045 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 les_4_task_1.py:45(freq_num2)

# Вариант 3: N = 10000
#          64506 function calls in 6.053 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    6.003    6.003    6.008    6.008 les_4_task_1.py:50(freq_num3)


'''Заключение:
Варианты 1 и 2 работают значительно быстрее при больших N, и их
скорости сопоставимы. Однако вариант 2 имеет меньшее количество
строк кода за счет использования библиотечного класса Counter.
Таким образом, для простого подсчета числа элементов, без
дополнительной обработки, это наиболее предпочтительный вариант
реализации. Вместе с тем, первый вариант является более гибким и
может быть адаптирован под задачу с минимальной потерей
производительности.
'''
