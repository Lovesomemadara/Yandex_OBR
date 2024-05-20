n: int = int(input())
m: int = int(input())

semolina: set[str] = set()
oatmeal: set[str] = set()
for _ in range(n):
    surname: str = input()
    semolina.add(surname)

for _ in range(m):
    surname: str = input()
    oatmeal.add(surname)

both: set[str] = semolina.intersection(oatmeal)

print(len(both) or 'Таких нет')
