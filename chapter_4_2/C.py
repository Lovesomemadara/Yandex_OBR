def gcd(*args) -> tuple | int:
    if len(args) == 1:
        return args[0]

    def find_gcd(a, b) -> int:
        while b:
            a, b = b, a % b
        return a

    res: int = args[0]
    for num in args[1:]:
        res = find_gcd(res, num)

    return res


print(gcd(36, 48, 156, 100500))
