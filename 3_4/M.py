from itertools import permutations

arrangements: list[str] = [
    ', '.join(i)
    for i in permutations([input() for _ in range(int(input()))])
]

print('\n'.join(sorted(arrangements)))
