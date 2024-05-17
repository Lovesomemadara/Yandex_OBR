n: int = int(input())

# data: list[str] = []
# for _ in range(n):
#     line: list[str] = input().split()
#     for item in line:
#         if item not in data:
#             data.append(item)
# print(*data, sep="\n")


data: set[str] = set()
for _ in range(n):
    line: set[str] = set(input().split())
    print(line)
    data.update(line)

print(*data, sep="\n")
