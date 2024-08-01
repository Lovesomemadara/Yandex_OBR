from typing import Callable


def answer(func: Callable):
    def inner(*args, **kwargs):
        result = f'Результат функции: {func(*args, **kwargs)}'

        return result

    return inner


@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
