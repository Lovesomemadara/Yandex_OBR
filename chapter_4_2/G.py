results: list[str] = []


def enter_results(*args) -> tuple[int, float]:
    results.extend(args)


def get_sum() -> tuple[int, float]:
    first_sum: int = sum(results[::2])
    second_sum: int = sum(results[1::2])
    return round(first_sum, 2), round(second_sum, 2)


def get_average() -> tuple[int, float]:
    first_avg: float = sum(results[::2]) / (len(results) // 2)
    second_avg: float = sum(results[1::2]) / (len(results) // 2)
    return round(first_avg, 2), round(second_avg, 2)


enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
