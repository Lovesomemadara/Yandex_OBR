n: int = int(input())

surnames_list: dict[str, int] = {}
for _ in range(n):
    surname: str = input()
    if surname not in surnames_list:
        surnames_list[surname] = 1
    else:
        surnames_list[surname] += 1

if len(surnames_list) == n:
    print('Однофамильцев нет')
else:
    for person, count in sorted(surnames_list.items()):
        if count > 1:
            print(f'{person} - {count}')
