results: list[str] = []


def enter_results(*args) -> None:
    global results
    results.extend(args)


def get_sum() -> tuple[int, float]:
    global results
    first_sum: int = sum(results[::2])
    second_sum: int = sum(results[1::2])
    return round(first_sum, 2), round(second_sum, 2)


def get_average() -> tuple[float, float]:
    global results
    first, second = get_sum()
    length: int = len(results) // 2

    first_avg: float = first / length
    second_avg: float = second / length
    return round(first_avg, 2), round(second_avg, 2)
    # или
    # return round(first / length, 2), round(second / length, 2)


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
