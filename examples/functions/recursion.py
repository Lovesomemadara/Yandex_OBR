# Рекурсия

# Факториал числа

n = 6
prod: int = 1
for i in range(1, n + 1):
    prod *= i

print(f"Факториал числа {n} равен {prod}")


# ------------------

def factorial(num: int) -> int:
    # Базовый случай
    if num == 1:
        return num

    return num * factorial(num - 1)


n: int = 5
print(f"Факториал числа {n} равен {factorial(n)}")

# ------------------
nums: list[int] = [1, 2, 3, 4, 5]


def recursive_sum(data: list[int]) -> int:
    # Базовый случай
    if not data:
        return 0
    return data[0] + recursive_sum(data[1:])


print(recursive_sum(nums))
