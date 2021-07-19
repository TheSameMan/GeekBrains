'''3. Массив размером 2m + 1, где m — натуральное число, заполнен
случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в
одной находятся элементы, которые не меньше медианы, в другой —
не больше медианы.
'''


# Naive method: O(n^2)
def median(a):
    while len(a) > 2:
        a.remove(min(a))
        a.remove(max(a))

    return a[0] if len(a) == 1 else (a[0] + a[1])/2

# Selection of kth element: O(n)
def kselect(a, k):
    from random import choice
    if len(a) == 1:
        return a[0]

    p = choice(a)

    left = [el for el in a if el < p]
    pivot = [el for el in a if el == p]
    right = [el for el in a if el > p]

    if k < len(left):
        return kselect(left, k)
    elif k < len(left) + len(pivot):
        return pivot[0]
    else:
        return kselect(right, k - len(left) - len(pivot))

# Median search: O(n)
def quick_median(a):
    if len(a) % 2:
        return kselect(a, len(a)//2)

    return (kselect(a, len(a)//2-1) + kselect(a, len(a)//2)) / 2


if __name__ == '__main__':
    from random import randint

    m = 10
    a = [randint(0, m//2) for _ in range(2 * m + 1)]

    print(f'Случайный список: {a}')
    print(f'Медиана: {quick_median(a)}')
