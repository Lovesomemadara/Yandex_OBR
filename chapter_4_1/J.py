def merge(t1: tuple[int], t2: tuple[int]) -> tuple[int]:
    result: list[int] = []
    i, j = 0, 0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            result.append(t1[i])
            i += 1
        else:
            result.append(t2[j])
            j += 1
    result.extend(t1[i:])
    result.extend(t2[j:])
    return tuple(result)


print(merge((1, 2), (3, 4, 5)))
