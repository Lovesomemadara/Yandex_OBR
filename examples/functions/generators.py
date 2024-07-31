# Генераторы
nums: list[int] = [1, 2, 3, 4, 5]

for n in nums:
    pass


def custom_gen(data: str | list):
    for item in data:
        yield item


for char in custom_gen('Hello'):
    print(char)


def custom_cycle(data: str | list | tuple):
    seen = []
    for item in data:
        yield item
        seen.append(item)

    while seen:
        for elem in seen:
            yield elem
