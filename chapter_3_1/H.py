line: list[int] = [
    input().lower().find('зайка') + 1
    for _ in range(int(input()))
]

for index in line:
    if index == 0:
        print('Заек нет =(')
        continue

    print(index)
