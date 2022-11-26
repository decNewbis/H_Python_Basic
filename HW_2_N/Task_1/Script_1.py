list_1 = []

while True:
    entered_text = input('Введіть ціле число або "/q" для завершення програми: ')
    try:
        if entered_text == '/q':
            print(f'Ви ввели {len(list_1)} парних чисел')
            break
        else:
            entered_text = int(entered_text)
            if entered_text % 2 == 0:
                list_1.append(entered_text)
    except ValueError:
        print('Ви ввели не вірне значення. Спробуйте ще раз.')
