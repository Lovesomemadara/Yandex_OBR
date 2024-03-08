nums: list[int] = [int(char) for char in input()]

current_digit = nums[0]
count = 1

for i in range(1, len(nums)):
    if nums[i] == current_digit:
        count += 1
    else:
        print(current_digit, count)
        current_digit = nums[i]
        count = 1

print(current_digit, count)
