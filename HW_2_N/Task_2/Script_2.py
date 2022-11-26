# example 1
def example_1():
    print('Example 1')
    list_1 = []
    while True:
        entered_text = input('Введіть ціле число для створення списку: ')
        try:
            for element in range(int(entered_text) + 1):
                list_1.append(element ** 3)
            print(f'Створений список: \n{list_1}')
            break
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


# example 2
def example_2():
    print('Example 2')
    while True:
        entered_text = input('Введіть ціле число для створення списку: ')
        try:
            list_1 = [x ** 3 for x in range(int(entered_text) + 1)]
            print(f'Створений список: \n{list_1}')
            break
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


example_1()
example_2()
