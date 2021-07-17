'''1. Пользователь вводит данные о количестве предприятий, их
наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''


from collections import OrderedDict

QUARTERS_IN_YEAR = 4

while True:
    try:
        if (n:= int(input('Введите количество предприятий: '))) <= 0:
            raise ValueError

        records = OrderedDict.fromkeys(input('Введите \
названия предприятий через запятую: ').split(', '))

        if (len_records := len(records)) != n:
            raise ValueError

    except ValueError:
        print('Некорректный ввод, повторите попытку.\n')
    else:
        break

print('Введите прибыль за каждый квартал через пробел.')

# finding average income
avg_income = 0
for k in records.keys():
    while True:
        try:
            quarters = tuple(map(int, input(f'{k}: ').split(' ')))

            if len(quarters) != QUARTERS_IN_YEAR:
                raise ValueError
        except ValueError:
            print('Некорректный ввод, повторите попытку.')
        else:
            break

    records[k] = sum(quarters)
    avg_income += records[k]

avg_income /= n

# splitting income values
left_records = OrderedDict()
for _ in range(len_records):
    income = records.popitem(last=False)

    if income[1] < avg_income:
        left_records[income[0]] = income[1]
    elif income[1] > avg_income:
        records[income[0]] = income[1]

print(f'\nСредняя прибыль: {avg_income:.2f}')

print('Предприятия с прибылью ниже среднего:', end=' ')
if len(left_records):
    print(*left_records.keys(), sep=', ')
else:
    print('Нет')

print('Предприятия с прибылью выше среднего:', end=' ')
if len(records):
    print(*records.keys(), sep=', ')
else:
    print('Нет')
