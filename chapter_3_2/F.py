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

both: set[str] = like_semolina.symmetric_difference(like_oatmeal)

if not both:
    print('Таких нет')
else:
    print(*(sorted(both)), sep='\n')
