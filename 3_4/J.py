from itertools import product

n: int = int(input())

players: list[str] = ['А', 'Б', 'В']
print(*players)
for item in product(
        list(range(1, n)), repeat=len(players)
):
    if sum(item) == n:
        print(*item)
