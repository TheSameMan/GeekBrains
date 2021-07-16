'''2. Написать два алгоритма нахождения i-го по счёту простого
числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
'''


if __name__ == "__main__":
    import cProfile

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime(n):
    if n <= 0:
        return 2

    idx, pr = 0, 2

    i = 3
    while idx != n - 1:
        if is_prime(i):
            idx, pr = idx + 1, i

        i += 1

    return pr


def get_sieve(n):
    primes = [True for i in range((n+1))]

    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * p, n+1, p):
                primes[i] = False

        p += 1

    res = []
    for p in range(2, n+1):
        if primes[p]:
            res.append(p)
    return res

def sieve(idx):
    if idx <= 0:
        return 2
    primes = get_sieve(idx)
    n = idx
    while len(primes) <= idx:
        n *= 2
        primes = get_sieve(n)

    return primes[idx-1]


if __name__ == "__main__":
    for i in [10, 100, 1000, 10000]:
        print(f'prime({i}):')
        cProfile.run('prime(i)')
    for i in [10, 100, 1000, 10000]:
        print(f'sieve({i}):')
        cProfile.run('sieve(i)')


# Результаты работы cProfile

# prime(10):
#          31 function calls in 0.000 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        27    0.000    0.000    0.000    0.000 les_4_task_2.py:12(is_prime)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:21(prime)
#
# prime(100):
#          543 function calls in 0.002 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       539    0.002    0.000    0.002    0.000 les_4_task_2.py:12(is_prime)
#         1    0.000    0.000    0.002    0.002 les_4_task_2.py:21(prime)
#
# prime(1000):
#          7921 function calls in 0.278 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      7917    0.275    0.000    0.275    0.000 les_4_task_2.py:12(is_prime)
#         1    0.003    0.003    0.278    0.278 les_4_task_2.py:21(prime)
#
# prime(10000):
#          104731 function calls in 33.782 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    104727   33.730    0.000   33.730    0.000 les_4_task_2.py:12(is_prime)
#         1    0.052    0.052   33.781   33.781 les_4_task_2.py:21(prime)
#
#
# sieve(10):
#          37 function calls in 0.000 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         3    0.000    0.000    0.000    0.000 les_4_task_2.py:37(get_sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:54(sieve)
#
# sieve(100):
#          304 function calls in 0.000 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         4    0.000    0.000    0.000    0.000 les_4_task_2.py:37(get_sieve)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:54(sieve)
#
# sieve(1000):
#          2044 function calls in 0.003 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         4    0.002    0.001    0.003    0.001 les_4_task_2.py:37(get_sieve)
#         1    0.000    0.000    0.003    0.003 les_4_task_2.py:54(sieve)
# sieve(10000):
#          30233 function calls in 0.060 seconds
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         5    0.046    0.009    0.059    0.012 les_4_task_2.py:37(get_sieve)
#         1    0.001    0.001    0.060    0.060 les_4_task_2.py:54(sieve)


# Результаты работы timeit

# Функция prime(10): 100 loops, best of 5: 15.5 usec per loop
# Функция prime(100): 100 loops, best of 5: 1.54 msec per loop
# Функция prime(1000): 100 loops, best of 5: 254 msec per loop
# Функция prime(10000): 100 loops, best of 5: 35 sec per loop

# Функция sieve(10): 100 loops, best of 5: 13.8 usec per loop
# Функция sieve(100): 100 loops, best of 5: 221 usec per loop
# Функция sieve(1000): 100 loops, best of 5: 2.47 msec per loop
# Функция sieve(10000): 100 loops, best of 5: 54 msec per loop

'''Заключение:
Функция sieve работает гораздо быстрее функции prime.
Видно, что функция sieve имеет сложность бликую к линейной O(n),
а функция prime - O(n^2)
'''