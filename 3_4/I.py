n: int = int(input())

for i in range(1, n + 1):
    row: list[str] = [str(i * j) for j in range(1, n + 1)]
    print(' '.join(row))
