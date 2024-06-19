nums: list[str] = [bin(int(x))[2:] for x in input().split()]

binary_statistics: list[dict[str, int]] = [{
    'digits': len(num),
    'units': num.count('1'),
    'zeros': num.count('0')
} for num in nums]

print(binary_statistics)
