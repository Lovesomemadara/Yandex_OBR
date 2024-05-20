n: int = int(input())
m: int = int(input())

semolina: set[str] = {input() for _ in range(n)}
oatmeal: set[str] = {input() for _ in range(m)}

both: int = len(semolina.symmetric_difference(oatmeal))

print(both or 'Таких нет')
