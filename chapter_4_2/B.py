def make_matrix(size: int, value: int = 0) -> list[list[int]]:
    if isinstance(size, int):
        size: tuple[int, int] = (size, size)
    width, height = size
    matrix: list[list[int]] = [
        [value for _ in range(width)] for _ in range(height)
    ]
    return matrix


print(make_matrix(3))
