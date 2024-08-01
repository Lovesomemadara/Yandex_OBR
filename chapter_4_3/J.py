def make_linear(data: list[list | int]) -> list:
    result: list[int] = []
    for item in data:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)

    return result


print(make_linear([1, [2, [3, 4]], 5, 6]))
