'''1. Подсчитать, сколько было выделено памяти под переменные в
ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов
идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по
памяти;
b. написать 3 варианта кода (один у вас уже есть);

проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде
разработки) вставить в виде комментариев в файл с кодом. Не
забудьте указать версию и разрядность вашей ОС и интерпретатора
Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

#Профилирование кода для задачи:
#4. Определить, какое число в массиве встречается чаще всего.

import os
import sys
import inspect
import re


print(os.uname().sysname, os.uname().machine)
print(sys.version)

def memprof(fun):
    """The decorator function adds additional memory
    profiling code to the function under test
    """
    def wrap(*fake_args):
        if inspect.isfunction(fun):
            # create a line indent
            def indent(line):
                count = 0
                for c in line:
                    if c != ' ':
                        break
                    count += 1

                return ' ' * count

            # check the uselessness of the string
            def iswaste(line):
                return True if re.match(r'(^\s*$)|(^\s*#+)', line) else False

            # check the return from the function
            def isreturn(line):
                return True if re.match(r'\s*return[\s+\w\'\"[{(]*', line) \
            else False

            # function to list of its strings
            code = inspect.getsourcelines(fun)[0][1:]

            for line in code:
                if line.lstrip().startswith('@'):
                    print('Too many decorators to process.')
                    return

            f_name = fun.__name__
            a_names = fun.__code__.co_varnames[:fun.__code__.co_argcount]
            v_names = fun.__code__.co_varnames[fun.__code__.co_argcount:]
            if not v_names:
                print(fun.__name__, 'profiling:')
                print('- variables not found.')
                return

            global show_size # is called in function under the test
            def show_size(x):
                size = sys.getsizeof(x)
                if hasattr(x.__class__, '__getitem__'):
                    if hasattr(x, '__iter__'):
                        if hasattr(x, 'items'):
                            for key, value in x.items():
                                size += show_size(key)
                                size += show_size(value)
                        elif not isinstance(x, str):
                            for item in x:
                                size += show_size(item)
                return size

            template = \
        'print("- ", show_size({v}), "bytes are allocated for {v}")'

            ret = False# return occured
            for i, line in enumerate(code[:]):
                if iswaste(line) and (i != len(code) - 1):
                    continue

                if isreturn(line):
                    # adding testing code
                    test_code = indent(line) + \
                'print("' + fun.__name__ + ' profiling:")\n'
                    for v in v_names:
                        test_code = ''.join((test_code, indent(line),
                                             template.format(v=v), '\n'))
                    code.insert(i, test_code)

                    ret = True
                elif not ret and (i == len(code) - 1):
                    # adding testing code
                    test_code = indent(line) + \
                'print("' + fun.__name__ + ' profiling:")\n'
                    for v in v_names:
                        test_code = ''.join((test_code, indent(line),
                                             template.format(v=v),'\n'))
                    code.insert(i, test_code)

            code = "\n".join(code)

            # a_names to string for exec
            str_args = ''
            for i in range(len(a_names)):
                if i != len(a_names) - 1:
                    str_args += a_names[i] + ', '
                else:
                    str_args += a_names[i]

            # execute the new function code
            exec(f'{code}{f_name}({str_args})')

        else:
            print('Function code error.')
    return wrap

from random import randint
a = [randint(0, 10) for _ in range(1000)]


@memprof
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

@memprof
def freq_num2(a):
    from collections import Counter
    mc = Counter(a).most_common(1)[0]
    return mc

@memprof
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

freq_num1(a)
freq_num2(a)
freq_num3(a)


# Linux x86_64
# 3.9.4 (default, Apr  9 2021, 16:34:09) 
# [GCC 7.3.0]
# freq_num1 profiling:
# -  1252 bytes are allocated for counts
# -  28 bytes are allocated for el
# -  108 bytes are allocated for max_item
# -  112 bytes are allocated for item
# freq_num2 profiling:
# -  1064 bytes are allocated for Counter
# -  108 bytes are allocated for mc
# freq_num3 profiling:
# -  24 bytes are allocated for num
# -  28 bytes are allocated for max_freq
# -  28 bytes are allocated for i
# -  28 bytes are allocated for frq
# -  28 bytes are allocated for j


'''Заключение. Видно, что наименьшее количество памяти выделено в
функции freq_num3. Для функции freq_num2 сложно определить точное
количество памяти, так как функция показывает размер самого класса
Counter. Если не учитывать этого, то наиболее выгодным является
использование функции freq_num2.'''
