from itertools import cycle, islice

porridges: list[str] = [input() for _ in range(int(input()))]

n: int = int(input())

porridge_cycle: cycle[str] = cycle(porridges)

for porridge in islice(porridge_cycle, n):
    print(porridge)
