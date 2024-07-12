from itertools import combinations

pairs: tuple[str] = zip(input().split(', '), input().split(', '))
for first, second in pairs:
    print(f'{first} - {second}')
