nums: list[int] = [int(input()) for _ in range(int(input()))]
degree: int = int(input())

result: list[int] = [num ** degree for num in nums]
print(*result, sep='\n')

# Option 2

# result: list[int] = []
# for num in nums:
#     result.append(num ** degree)
#
# for i in result:
#     print(i)
