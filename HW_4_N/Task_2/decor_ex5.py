def validate(*types):
    def decorator(func_):
        def wrap(*args):
            for value, value_type in zip(args, types):
                if not isinstance(value, value_type):
                    raise TypeError(f"type a expected: {value_type}, but got {type(value)}")
            return func_(*args)
        return wrap
    return decorator


@validate((int, float), (list, tuple), (int, float))
def func(a: int | float, b: list | tuple, c: int | float) -> list:
    pass


@validate((list, tuple), (list, tuple), (int, float))
def func2(a, b, c) -> list:
    pass


@validate((list, tuple), (list, tuple), (int, float), (list, tuple), (str, set))
def func3(*args) -> list:
    pass


func(1, [2], 3)
func2([1], [2], 3)
func3((1,), [2], 3, [8], '3')
