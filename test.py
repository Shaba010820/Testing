
def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for key, value in kwargs.items():
            must_have_type = annotations.get(args)
            if must_have_type and not isinstance(value, must_have_type):
                raise TypeError(f'Ошибка в типе данных - ожидалось {must_have_type.__name__}, '
                                f'получил {type(value)}')

        for i, (key, value) in enumerate(zip(annotations.keys(), args)):
            must_have_type = annotations[key]
            if not isinstance(value, must_have_type):
                raise TypeError(f'Ошибка в типе данных - ожидалось {must_have_type.__name__}, '
                                f'получил {type(value)}')

        return func(*args, **kwargs)

    return wrapper
@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))
print(sum_two(1, 2.4))
