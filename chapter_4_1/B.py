def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


# result = gcd(12, 45)
# print(f'result = {result}')
