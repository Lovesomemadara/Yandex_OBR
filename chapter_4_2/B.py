def make_matrix(size, value=0):
    if isinstance(size, int):
        size = (size, size)
    width, height = size
    matrix: list[list[int]] = [
        [value for _ in range(width)] for _ in range(height)
    ]
    return matrix


# result = make_matrix(3)
# print(f'result = {result}')
