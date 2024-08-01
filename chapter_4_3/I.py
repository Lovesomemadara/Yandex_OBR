def cycle(data: str | list | tuple) -> int:
    seen: list[int] = []
    for item in data:
        yield item
        seen.append(item)

    while seen:
        for elem in seen:
            yield elem


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
