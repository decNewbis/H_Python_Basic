# example 1
def example_1():
    print('Example 1')
    while True:
        try:
            operand_1 = float(input('Введіть перше число: '))
            operator_math = input('Введіть один з операторів із списку [+, -, *, /]: ')
            operand_2 = float(input('Введіть друге число: '))
            if operator_math == '+':
                print(round(operand_1 + operand_2, 2))
                break
            elif operator_math == '-':
                print(round(operand_1 - operand_2, 2))
                break
            elif operator_math == '*':
                print(round(operand_1 * operand_2, 2))
                break
            elif operator_math == '/':
                if operand_2 != 0:
                    print(round(operand_1 / operand_2, 2))
                    break
                else:
                    print('На нуль ділити не можна!')
            else:
                print('Щось пішло не так, спробуй ще раз.')
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


# example 2
def example_2():
    print('Example 2')
    while True:
        try:
            operand_1 = float(input('Введіть перше число: '))
            operator_math = input('Введіть один з операторів із списку [+, -, *, /]: ')
            operand_2 = float(input('Введіть друге число: '))
            if operator_math == '+':
                print(round(operand_1 + operand_2, 2))
                break
            elif operator_math == '-':
                print(round(operand_1 - operand_2, 2))
                break
            elif operator_math == '*':
                print(round(operand_1 * operand_2, 2))
                break
            elif operator_math == '/':
                print(round(operand_1 / operand_2, 2))
                break
            else:
                print('Щось пішло не так, спробуй ще раз.')
        except ZeroDivisionError:
            print('На нуль ділити не можна!')
        except ValueError:
            print('Ви ввели не вірне значення. Спробуйте ще раз.')


example_1()
example_2()
