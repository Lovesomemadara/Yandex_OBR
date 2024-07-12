from itertools import combinations

names: list[str] = [input() for _ in range(int(input()))]

pairs: list[str] = list(combinations(names, 2))

for first, second in pairs:
    print(f'{first} - {second}')
