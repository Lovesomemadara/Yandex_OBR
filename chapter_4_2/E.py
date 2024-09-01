def to_string(*args, sep: str = ' ', end: str = '\n') -> str:
    return sep.join(map(str, args)) + end

# data = [7, 3, 1, "hello", (1, 2, 3)]
# result = to_string(*data, sep=", ", end="!")
# print(f'result = {result}')
