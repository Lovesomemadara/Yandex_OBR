def recursive_digit_sum(num: int, res: int = 0) -> int:
    if not num:
        return res
    res += num % 10
    num //= 10
    return recursive_digit_sum(num, res)


print(recursive_digit_sum(123))
