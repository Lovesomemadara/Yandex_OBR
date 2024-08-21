from sys import stdin

difference: list[int] = []

for i, elem in enumerate(stdin.read().split()):
    if i % 3 != 0:
        difference.append(int(elem))

diff: int = 0
for num in range(0, len(difference)):
    if num % 2 != 0:
        diff += difference[num] - difference[num - 1]

print(round(diff / (len(difference) / 2)))
