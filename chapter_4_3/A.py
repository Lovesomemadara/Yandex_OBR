def recursive_sum(*args) -> int:
    if not args:
        return 0
    return args[0] + recursive_sum(*args[1:])


print(recursive_sum(1, 2, 3))
