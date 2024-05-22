n: int = int(input())

surname_porridge: dict[str, str] = {}

for _ in range(n):
    child: list[str] = input().split()
    surname_porridge[child[0]] = child[1]

wanted_porridge: str = input()
like_porridge: list[str] = []
for item in surname_porridge.items():
    surname, porridge = item
    if wanted_porridge == porridge:
        like_porridge.append(surname)

if not like_porridge:
    print('Таких нет')
else:
    print(*(sorted(like_porridge)), sep='\n')
