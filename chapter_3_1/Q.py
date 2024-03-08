line: str = input().replace(' ', '').lower()

if line == line[::-1]:
    print('YES')
else:
    print('NO')

# Option 2
print(
    'YES' if line == line[::-1] else 'NO'
)
