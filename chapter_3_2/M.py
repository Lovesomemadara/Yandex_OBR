n: int = int(input())
available_dishes: set[str] = {input() for _ in range(n)}

m: int = int(input())
weekly_dishes: list = [set() for _ in range(m)]
# weekly_dishes: set = set()

for i in range(m):
    num_dishes: int = int(input())
    for _ in range(num_dishes):
        weekly_dishes[i].add(input())
        # weekly_dishes.add(input())

new_dishes: list[str] = sorted(available_dishes - set.union(*weekly_dishes))
# new_dishes: list[str] = sorted(available_dishes - weekly_dishes)

if new_dishes:
    print('\n'.join(new_dishes))
else:
    print('Готовить нечего')
