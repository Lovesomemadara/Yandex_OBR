def gcd(*numbers):
    if len(numbers) == 1:
        return numbers[0]

    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    res = numbers[0]
    for num in numbers[1:]:
        res = find_gcd(res, num)

    return res


# result = gcd(3)
# print(f'result = {result}')
