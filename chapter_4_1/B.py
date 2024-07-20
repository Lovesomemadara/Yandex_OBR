def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


# result = gcd(12, 45)
# print(f'result = {result}')
