def begin_coroutine(func):
    def wrapper(*args, **kwargs):
        avg_ = func(*args, **kwargs)
        next(avg_)
        return avg_
    return wrapper


@begin_coroutine
def average():
    avg_ = 0
    nums_list = []
    while True:
        a = yield avg_
        avg_ += a
        nums_list.append(a)
        if len(nums_list) > 0:
            avg_ = sum(nums_list) / len(nums_list)


if __name__ == '__main__':
    avg = average()

    assert avg.send(1) == 1.0  # [1] -> 1.0
    assert avg.send(2) == 1.5  # [1, 2] -> 1.5
    assert avg.send(3) == 2.0  # [1, 2, 3] -> 2.0
    assert avg.send(4) == 2.5  # [1, 2, 3, 4] -> 2.5
    assert avg.send(5) == 3.0  # [1, 2, 3, 4, 5] -> 3.0
