set_1 = {11, 12, 32, 33, 1, 2, 3}

# example 1
set_2 = set(map(int, input('Введіть свій ряд цілих чисел через кому: ').split(',')))
number_coincidence = set_1.intersection(set_2)
print(f"example 1: Кількість збігів: {len(number_coincidence)}")

# example 2
print(f"example 2: Кількість збігів: {len(set_1 & set_2)}")
