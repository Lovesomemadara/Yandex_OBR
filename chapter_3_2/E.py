n: int = int(input())
m: int = int(input())

like_semolina: set[str] = set()
like_oatmeal: set[str] = set()
for _ in range(n + m):
    child: str = input()
    if child in like_semolina:
        like_oatmeal.add(child)
    else:
        like_semolina.add(child)

both: int = len(like_semolina.symmetric_difference(like_oatmeal))

print(both or 'Таких нет')
