objects: set[str] = set()
while True:
    line: list[str] = input().split()
    if not line:
        break
    for item in range(len(line)):
        if line[item] == 'зайка':
            if item > 0:
                objects.add(line[item - 1])
            if item < len(line) - 1:
                objects.add(line[item + 1])

print('\n'.join(objects))
