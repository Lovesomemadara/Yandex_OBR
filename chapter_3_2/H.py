n: int = int(input())

surname_porridge: dict[str, str] = {}
for _ in range(n):
    child, *porridge = input().split()
    surname_porridge[child] = porridge

like_porridge: list[str] = []
wanted_porridge: str = input()
for child, porridge in surname_porridge.items():
    if wanted_porridge in porridge:
        like_porridge.append(child)

if not like_porridge:
    print('Таких нет')
else:
    print(*(sorted(like_porridge)), sep='\n')
