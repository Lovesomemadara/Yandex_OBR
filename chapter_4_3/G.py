def same_type(func):
    def wrapper(*args):
        types = set(type(arg) for arg in args)
        if len(types) > 1:
            print('Обнаружены различные типы данных')

            return 'Fail'

        return func(*args)

    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
