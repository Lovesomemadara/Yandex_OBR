from itertools import permutations

arrangements = [', '.join(i) for i in permutations([input() for _ in range(int(input()))], 3)]

print('\n'.join(sorted(arrangements)))
