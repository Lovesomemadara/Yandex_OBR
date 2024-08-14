# №1
def number_length(x: int) -> int:
    return len(str(abs(x)))


# №2
def number_length(x: int) -> int:
    if x == 0:
        return 1

    count: int = 0
    x: int = abs(x) if x < 0 else x
    # x: int = abs(x)  # или просто без проверки
    while x > 0:
        count += 1
        x //= 10

    return count


input_data: list[int] = [12345, -12, 0, 123]
expected_data: list[int] = [5, 2, 1, 3]

for elem, expected in zip(input_data, expected_data):
    result = number_length(elem)
    assert result == expected, f"Ожидается {result}, получено {expected}"

print('Ok!')
