'''5. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.
'''


a = int(input('Введите номер буквы\n'))
if 1 <= a <= (ord('z') - ord('a') + 1):
    print(chr(a+ord('a')-1))
else:
    print('Некорректный ввод')
