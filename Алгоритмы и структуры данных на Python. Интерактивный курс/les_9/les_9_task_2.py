'''2. Закодируйте любую строку по алгоритму Хаффмана.'''


#The algorithm doesn't store the entire tree in memory, only the current layer
def huffman_code(message):
    if not isinstance(message, str):
        return None

    if 'Counter' not in dir():
        from collections import Counter

    freq_table = Counter(message)
    code_table = dict.fromkeys(freq_table.keys(), '')

    if len(freq_table) == 1:
        code_table[freq_table.most_common()[0][0]] = '0'
        return code_table

    while len(freq_table) > 1:
        left_key, left_value = None, float('inf')
        right_key, right_value = None, float('inf')

        for key, value in freq_table.items():
            if value < max(left_value, right_value):
                if left_value < right_value:
                    right_key, right_value = key, value
                else:
                    left_key, left_value = key, value

        for char in left_key:
            code_table[char] = '0' + code_table[char]
        for char in right_key:
            code_table[char] = '1' + code_table[char]

        freq_table[left_key + right_key] = \
            freq_table.pop(left_key) + freq_table.pop(right_key)

    return code_table


print('Кодирование произвольной строки по алгоритму Хаффмана.')

if len(message := input('Введите строку: ')):
    code_map = huffman_code(message)

    msg, len_msg = '', 0
    code, len_code = '', 0
    for char in message:
        bins = bin(ord(char))
        msg += bins + ' '
        len_msg += len(bins) - 2# except 0b

        code += '0b' + code_map[char] + ' '
        len_code += len(code_map[char])

    print(f'Двоичный код строки: {msg}\nКод Хаффмана: {code}')
    print(f'Коэффициент сжатия (без таблицы): {len_msg/len_code:.3f}')
