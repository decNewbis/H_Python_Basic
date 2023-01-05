def arithmetical_gen(d: int | float):
    current_val = 0
    while True:
        yield current_val
        current_val += d


def arithmetical_gen_2(start_point: int | float, d: int | float):
    current_val = start_point
    while True:
        yield current_val
        current_val += d


if __name__ == '__main__':
    a_gen = arithmetical_gen(10)
    for el in range(11):
        print(next(a_gen))
    print('-' * 20)
    a_gen_2 = arithmetical_gen_2(-50, 10)
    for el in range(11):
        print(next(a_gen_2))

