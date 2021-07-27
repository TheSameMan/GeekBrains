'''2. Написать программу сложения и умножения двух
шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''


from collections import deque

D = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
     '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
H = {k: v for v, k in D.items()}

def summ(a, b):
    a = deque(a, maxlen=len(a))
    b = deque(b, maxlen=len(b))
    s = deque()

    c = 0
    i = 0
    while i < a.maxlen or i < b.maxlen:
        ai = D[a[-1] if i < a.maxlen else '0']
        bi = D[b[-1] if i < b.maxlen else '0']

        n = ai + bi + c
        c = n // 16
        r = n % 16

        s.appendleft(H[r])

        a.rotate(1)
        b.rotate(1)

        i += 1

    if c:
        s.appendleft(H[c])

    while s[0] == '0' and len(s) > 1:
        s.popleft()

    return list(s)


def mult(a, b):
    a = deque(a, maxlen=len(a))
    b = deque(b, maxlen=len(b))
    s = deque()

    i = 0
    tmp = deque()
    while i < b.maxlen:

        c = 0
        for _ in range(a.maxlen):
            ai, bi = D[a[-1]], D[b[-1]]

            n = ai * bi + c
            c = n // 16
            r = n % 16

            a.rotate(1)

            tmp.appendleft(H[r])

        if c:
            tmp.appendleft(H[c])

        for _ in range(i):
            tmp.append('0')

        s = summ(s, tmp)

        b.rotate(1)
        tmp.clear()
        i += 1

    return list(s)

try:
    nums = input('Введите два шестнадцатеричных числа через пробел:\
 ').split(' ')

    a = list(nums[0].upper())
    b = list(nums[1].upper())

    for el in a:
        if el not in D:
            raise ValueError
    for el in b:
        if el not in D:
            raise ValueError

    print(f'Сумма чисел: {summ(a, b)}')
    print(f'Произведение чисел: {mult(a, b)}')

except ValueError:
    print('Неверный ввод')
except IndexError:
    print('Неверный ввод')
