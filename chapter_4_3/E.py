from typing import Callable


def result_accumulator(func: Callable):
    results: dict = {}

    def inner(*args, method="accumulate", **kwargs):
        if method == "accumulate":
            if func not in results:
                results[func] = []
            results[func].append(func(*args, **kwargs))

            return None

        elif method == "drop":
            if func in results:
                res: list[str] = results[func]
                del results[func]
                return res
            else:
                return []
        else:
            return func(*args, **kwargs)

    return inner


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))
