from itertools import permutations

products_list: list[str] = [
    i for _ in range(int(input()))
    for i in input().split(', ')
]
products_list.sort()

for item in permutations(products_list, r=3):
    print(', '.join(item))
