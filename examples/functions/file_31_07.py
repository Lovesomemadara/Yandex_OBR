# Анонимные функции

def two_sum(a: int, b: int):
    return a + b


print(two_sum(10, 4))

two_sum_short = lambda first, second: first + second
print(two_sum_short(5, 6))


# ---------------
def by_last_char(item: str):
    # return item[-1]
    return (item[-1], len(item))


fruits: list[str] = ["яблоко", "мандарины", "апельсин", "киви", "банан"]
# fruits.sort(key=by_last_char)
# fruits.sort(key=lambda fruit: fruit[-1])
fruits.sort(key=lambda fruit: (fruit[-1], len(fruit)))
print(fruits)


# Ключевое слово raise

def validate_num(number: int):
    if number <= 0:
        raise ValueError("Укажите натуральное число")

    if not isinstance(number, int):
        raise TypeError("Укажите целое число")


def factorial(num: int) -> int:
    validate_num(num)
    # Базовый случай
    if num == 1:
        return num

    return num * factorial(num - 1)

# factorial(-1)
# factorial(5.5)
