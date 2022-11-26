# example 1
def example_1():
    print('Example 1')
    list_1 = []
    sum_el = 0
    while True:
        entered_text = input('Введіть будь-яке число або "/q" для завершення програми: ')
        try:
            if entered_text == '/q':
                for element in list_1:
                    sum_el += element
                iter_el = len(list_1)
                if iter_el < 1:
                    iter_el = 1
                print(f'Середнє арифметичне значення введених чисел до сотих: {round(sum_el / iter_el, 2)} ')
                break
            else:
                entered_text = float(entered_text)
                list_1.append(entered_text)
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


# example 2
def example_2():
    print('Example 2')
    iter_el = 0
    sum_el = 0
    while True:
        entered_text = input('Введіть будь-яке число або "/q" для завершення програми: ')
        try:
            if entered_text == '/q':
                if iter_el < 1:
                    iter_el = 1
                print(f'Середнє арифметичне значення введених чисел до сотих: {round(sum_el / iter_el, 2)} ')
                break
            else:
                sum_el += float(entered_text)
                iter_el += 1
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


example_1()
example_2()
