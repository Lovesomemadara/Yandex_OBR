def recursive_digit_sum(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return recursive_digit_sum(num, res)


result = recursive_digit_sum(123)
print(result)
