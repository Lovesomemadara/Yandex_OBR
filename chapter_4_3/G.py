from typing import Callable


def same_type(func: Callable):
    def inner(*args):
        types: type[int, float, str] = set(type(arg) for arg in args)
        if len(types) > 1:
            print('Обнаружены различные типы данных')

            return 'Fail'

        return func(*args)

    return inner


@same_type
def a_plus_b(a: int, b: int) -> int:
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
