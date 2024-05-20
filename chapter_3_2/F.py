n: int = int(input())
m: int = int(input())

semolina: set[str] = {input() for _ in range(n)}
oatmeal: set[str] = {input() for _ in range(m)}

both: set[str] = semolina.symmetric_difference(oatmeal)

if not both:
    print('Таких нет')
else:
    print(*(sorted(both)), sep='\n')
