'''5. Вывести на экран коды и символы таблицы ASCII, начиная с
символа под номером 32 и заканчивая 127-м включительно. Вывод
выполнить в табличной форме: по десять пар «код-символ» в каждой
строке.
'''


START, END = 32, 127
PAIR_NUM = 10

for j in range(PAIR_NUM):
    pairs = ''

    first = START + PAIR_NUM * j
    for i in range(first, first+PAIR_NUM):
        if i > END:
            break
        pairs += '{0:>3} {1:<3}'.format(str(i), chr(i))

    print(pairs)
