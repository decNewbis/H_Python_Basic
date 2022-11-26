import math


# example 1
def hypotenuse_len(leg_1, leg_2):
    result = math.sqrt(sum((math.pow(leg_1, 2), math.pow(leg_2, 2))))
    return round(result, 3)


# example 2
def hypotenuse_len_2(leg_1, leg_2):
    result = (leg_1 ** 2 + leg_2 ** 2) ** 0.5
    return round(result, 3)


print(f'example 1: Довжина гіпотенузи: {hypotenuse_len(2.5, 2)}')
print(f'example 2: Довжина гіпотенузи: {hypotenuse_len_2(2.5, 2)}')
