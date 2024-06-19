objects: dict[str, int] = {}
while True:
    line: list[str] = input().split()
    if not line:
        break
    for item in line:
        if item not in objects:
            objects[item] = 1
        else:
            objects[item] += 1
        # objects[item] = objects.get(item, 0) + 1

for item, count in objects.items():
    print(f'{item} {count}')
