def recursive_sum(*nums):
    if not nums:
        return 0
    return nums[0] + recursive_sum(*nums[1:])


result = recursive_sum(1, 2, 3)
print(result)
