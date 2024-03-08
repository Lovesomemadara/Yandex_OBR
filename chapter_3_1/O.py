nums: list[int] = [int(x) for x in input().split()]

gcd_result: int = nums[0]
for i in range(1, len(nums)):
    a: int = gcd_result
    b: int = nums[i]
    while b:
        a, b = b, a % b
    gcd_result = a

print(gcd_result)
