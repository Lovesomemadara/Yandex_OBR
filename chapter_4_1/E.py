def split_numbers(nums: str) -> tuple:
    return tuple(map(int, nums.split()))


print(split_numbers('1 -2 3 -4 5'))
