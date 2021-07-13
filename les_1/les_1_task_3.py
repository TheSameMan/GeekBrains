'''3. Написать программу, которая генерирует в указанных
пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
'''


from random import randint, uniform

a, b = input('Введите нижнюю и верхнюю границы\n').split(' ')
a, b = min(a, b), max(a, b)

if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    print(randint(a, b))
elif a.isalpha() and b.isalpha():
    a, b = ord(a), ord(b)
    print(chr(randint(a, b)))
elif not( (a.isdigit() or b.isdigit()) and (a.isalpha() or b.isalpha()) ):
    a, b = float(a), float(b)
    print(uniform(a, b))
