dict_1 = {
    1: [1, 2, 3, 4, 5],
    2: [2, 2, 2, 2],
    3: [1]
}

# example 1
key_number_1 = int(input(f'example 1: Виберіть число зі списку [1, 2, 3]: '))
print(f'example 1: {dict_1[key_number_1]}')


# example 2
def key_number_2():
    result = None
    while result not in dict_1:
        result = int(input(f'example 2: Виберіть число зі списку [1, 2, 3]: '))
    print(f'example 2: {dict_1[result]}')


key_number_2()
