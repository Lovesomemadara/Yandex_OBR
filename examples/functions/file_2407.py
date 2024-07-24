from typing import Callable


def is_equal(first: str, second: str) -> bool:
    return first == second


def is_correct_len(first: str) -> bool:
    return 8 <= len(first) <= 255


def password(password_1: str, password_2: str) -> bool:
    calls: tuple[bool, ...] = (
        is_equal(first=password_1, second=password_2),
        is_correct_len(first=password_1)
    )

    return all(calls)


# print(password("qwerty123", "Qwerty123"))

# -----------------------

# Функции высшего порядка

def my_printer(func: Callable) -> None:
    func("Hello, World", end="")


# my_printer(print)


# --------

def custom_map(func: Callable,
               data: list | tuple | set | frozenset) -> list:
    result: list = []
    for elem in data:
        elem = func(elem)
        result.append(elem)

    return result


# nums: list[int] = list(map(int, input().split()))
# nums: list[int] = list(
#     custom_map(func=int, data=input().split())
# )
# print(nums)

# 9 10 43 -12 65

# --------

def by_last_letter(item):
    return item[-1]


fruits: list[str] = ["Яблоко", "Бананы", "Апельсин", "Мандарины", "Киви"]


# print(sorted(fruits, key=by_last_letter))


def custom_min(data: list | tuple, key: None = None):
    # TODO:
    pass


def custom_max(data: list | tuple, key=None):
    # TODO:
    pass


invalid_nums: list[str] = ["101", "9", "-6", "99", "437"]

# print(min(invalid_nums, key=int))
# print(max(invalid_nums, key=int))
