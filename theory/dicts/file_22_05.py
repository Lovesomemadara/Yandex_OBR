n = int(input())

for _ in range(n):
    # line: list[str] = input().split(maxsplit=1)
    name, *others = input().split()

    print(name, others)
