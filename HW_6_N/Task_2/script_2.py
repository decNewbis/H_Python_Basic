def generator_id(prefix=None):
    curr_id = 1
    while True:
        if prefix:
            result = f'{prefix}-{curr_id}'
        else:
            result = f'{curr_id}'
        yield result
        curr_id += 1


if __name__ == '__main__':
    gen_id = generator_id('ID')
    assert next(gen_id) == 'ID-1'
    assert isinstance(next(gen_id), str)
    assert next(gen_id) == 'ID-3'

    gen_id = generator_id('INTERNAL-ID')
    assert next(gen_id) == 'INTERNAL-ID-1'
    assert isinstance(next(gen_id), str)
    assert next(gen_id) == 'INTERNAL-ID-3'

    gen_id = generator_id()
    assert next(gen_id) == '1'
    assert isinstance(next(gen_id), str)
    assert next(gen_id) == '3'
