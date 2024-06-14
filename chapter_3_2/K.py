n: int = int(input())

surnames_list: dict[str, int] = {}
for _ in range(n):
    surname: str = input()
    if surname not in surnames_list:
        surnames_list[surname] = 1
    else:
        surnames_list[surname] += 1

namesakes: int = 0
for namesake, count in surnames_list.items():
    if int(count) > 1:
        namesakes += count

print(namesakes)
