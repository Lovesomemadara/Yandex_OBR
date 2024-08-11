# try - пробовать
# except - кроме
# else - тогда
# finally - конец

# -------------------

"""
try:
    ...
except ...:
    ...
else:
    ...
finally:
    ...
"""


def example():
    try:
        data = int(input('Введите целое число: '))
    except (ValueError, KeyboardInterrupt) as err:
        print(f'Тип ошибка: {err}')
        return False
    except Exception as err:
        print(f'Что-то пошло не так: {err}')
    else:
        if data != 0:
            print(2 / data)
        else:
            print('Деление на ноль!')
    finally:
        print('Завершение!')


example()
