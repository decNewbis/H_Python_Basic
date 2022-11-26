# example 1
def max_min_sum(*args):
    return sum((min(args), max(args)))


# example 2
def min_2(*args):
    result = args[0]
    for element in args:
        if element < result:
            result = element
    return result


def max_2(*args):
    result = args[0]
    for element in args:
        if element > result:
            result = element
    return result


def max_min_sum_2(*args):
    return sum((min_2(*args), max_2(*args)))


# example 3
def max_min_sum_3(*args):
    list_1 = list(args)
    list_1.sort()
    min_val = list_1[0]
    max_val = list_1[-1]
    return sum((min_val, max_val))


print(f'example 1: {max_min_sum(0, 2.5, 3.5, 2, 2, -1, 2, -5, 15)}')
print(f'example 2: {max_min_sum_2(0, 2.5, 3.5, 2, 2, -1, 2, -5, 15)}')
print(f'example 3: {max_min_sum_3(0, 2.5, 3.5, 2, 2, -1, 2, -5, 15)}')
