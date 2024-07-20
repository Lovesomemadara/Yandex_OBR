results: list[str] = []


def enter_results(*data):
    results.extend(data)


def get_sum():
    first_sum = sum(results[::2])
    second_sum = sum(results[1::2])
    return round(first_sum, 2), round(second_sum, 2)


def get_average():
    first_avg = sum(results[::2]) / (len(results) // 2)
    second_avg = sum(results[1::2]) / (len(results) // 2)
    return round(first_avg, 2), round(second_avg, 2)

# enter_results(1, 2, 3, 4, 5, 6)
# print(get_sum(), get_average())
# enter_results(1, 2)
# print(get_sum(), get_average())
