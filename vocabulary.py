def letter(word):
    word_low = word.lower()
    symbol_1 = "'"
    symbol_2 = '"'
    symbol_3 = '1234567890 +-*/|\=-_()[]{}?!.,:;@#$%^<>`~№«»©~¡¢£¤¥¦§®¿×÷˄˅–'
    alphabet = f'{symbol_1}{symbol_2}{symbol_3}'
    letters = dict()
    for c in word_low:
        if c in alphabet:
            pass
        else:
            letters[c] = letters.get(c, 0) + 1
    for key, value in letters.items():
        print(f'{key} = {value}')


def words(text):
    text = text.replace(',', '')  # Забираєм символи
    text = text.replace('.', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('–', '')

    text = text.replace('1', '')
    text = text.replace('2', '')
    text = text.replace('3', '')
    text = text.replace('4', '')
    text = text.replace('5', '')
    text = text.replace('6', '')
    text = text.replace('7', '')
    text = text.replace('8', '')
    text = text.replace('9', '')
    text = text.replace('0', '')

    text = text.replace('«', '')
    text = text.replace('»', '')
    text = text.replace('<', '')
    text = text.replace('>', '')
    text = text.replace('"', '')
    text = text.replace("'", '')

    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('{', '')
    text = text.replace('}', '')

    text = text.replace('+', '')
    text = text.replace('-', '')
    text = text.replace('*', '')
    text = text.replace('/', '')
    text = text.replace('=', '')

    text = text.lower()
    lin = text.split(' ')  # Розбивання речення на слова

    if '' in lin:  # Якшо речення має пропуски('')  у списку чи не має їх

        number = lin.count('')  # Рахуєм порожні значення('')
        for i in range(0, number):  # Забрираєм із списка порожні значення('')
            lin.remove('')

        new_lin = []  # Забираєм повторки і вибирає тільки слова які мають > 3 букв
        if lin:
            for a in lin:
                a_len = len(a)
                if a_len > 3:
                    if a not in new_lin:
                        new_lin.append(a)
                    else:
                        pass
                else:
                    pass
        else:
            print('Помилка')

        lin_sort = sorted(new_lin)  # Сортуєм слова

        lin_sort_len = len(lin_sort)  # Виводим словник
        for w in range(0, lin_sort_len):
            print(lin_sort[w])
    else:
        new_lin = []  # Забираєм повторки і вибирає тільки слова які мають > 3 букв
        if lin:
            for a in lin:
                a_len = len(a)
                if a_len > 3:
                    if a not in new_lin:
                        new_lin.append(a)
                    else:
                        pass
                else:
                    pass
        else:
            print('Помилка')

        lin_sort = sorted(new_lin)  # Сортуєм слова

        lin_sort_len = len(lin_sort)  # Виводим словник
        for w in range(0, lin_sort_len):
            print(lin_sort[w])


while True:
    print('''Виберіть номер дії:
1) Обчислення букв.
2) Створення словника.
3) Завершити.''')
    dia = str(input('> '))

    if dia == '1':
        sentence = str(input('Ведіть текст: '))
        letter(sentence)
    elif dia == '2':
        sentence = str(input('Ведіть текст: '))
        words(sentence)
    elif dia == '3':
        break
    else:
        print('Помилка...')
    print()