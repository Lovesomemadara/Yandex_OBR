def cycle(nums: list):
    pass


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
