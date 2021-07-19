'''1. Отсортируйте по убыванию методом пузырька одномерный
целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный
массивы.
'''


from random import randint

a = [randint(-100, 100) for _ in range(-100, 100)]
print(f'Исходный массив:\n{a}')
def bubble_sort(a):
    run = True
    k, l = 0, 1
    while run:
        run = False
        for i in range(k, len(a) - l):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                run = True
                if i == k and k > 0:
                    k -= 1
            else:
                if i == k:
                    k += 1

            if i + 1 == len(a) - l:
                l += 1

bubble_sort(a)
print(f'Отсортированный массив:\n{a}')
