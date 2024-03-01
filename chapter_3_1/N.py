nums: list[int] = [int(x) for x in input().split()]
degree: int = int(input())

result: list[str] = []
for num in nums:
    result.append(str(num ** degree))
print(' '.join(result))
