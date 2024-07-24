from typing import Callable


def more_info(func: Callable):
    def inner(*args, **kwargs):
        print('Начинаются вычисления')
        result = func(*args, **kwargs)
        print('Готово!')

        return result

    return inner


@more_info
def add_two_sum(a: int, b: int) -> int:
    return a + b


print(add_two_sum(5, 10))
