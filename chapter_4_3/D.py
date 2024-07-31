from typing import Callable


def answer(func: Callable):
    def wrapper(*args, **kwargs):
        result = f'Результат функции: {func(*args, **kwargs)}'

        return result
    return wrapper


@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
