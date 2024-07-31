def fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        yield a
        a, b = b, a + b


print(*fibonacci(5))
