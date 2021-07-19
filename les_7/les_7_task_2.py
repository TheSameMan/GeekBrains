'''2. Отсортируйте по возрастанию методом слияния одномерный
вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
'''


from random import uniform

a = [uniform(0, 50) for _ in range(0, 50)]

print(f'Исходный массив:\n{a}')

def merge_sort(a):
    if len(a) <= 1:
        return a

    p = len(a)//2
    left = a[:p]
    right = a[p:]

    left = merge_sort(left)
    right = merge_sort(right)

    res = []

    i, j = 0, 0
    while True:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

        if i == len(left):
            res.extend(right[j:])
            break

        if j == len(right):
            res.extend(left[i:])
            break

    return res


print(f'Отсортированный массив:\n{merge_sort(a)}')
