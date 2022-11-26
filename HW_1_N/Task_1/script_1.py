list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# example 1
print(f'example 1: {list_1[::2]}')

# example 2
list_2 = list_1[::2]
print(f'example 2: {list_2}')

# example 3
print('example 3: ')
for element in list_2:
    print(f'\telement {list_2.index(element)}: {element}')
