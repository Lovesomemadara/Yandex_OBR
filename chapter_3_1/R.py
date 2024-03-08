nums: list[int] = [int(char) for char in input()]

current_digit: int = nums[0]
count: int = 1

for i in range(1, len(nums)):
    if nums[i] == current_digit:
        count += 1
    else:
        print(current_digit, count)
        current_digit = nums[i]
        count = 1

print(current_digit, count)

# Option 2
line: str = input()

length: int = len(line)
count: int = 1

for i in range(length):
    if i == length - 1:
        print(line[i], count)
        break
    if line[i] == line[i + 1]:
        count += 1
    else:
        print(line[i], count)
        count = 1
