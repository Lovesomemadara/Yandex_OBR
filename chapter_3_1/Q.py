line: str = input().replace(' ', '').lower()

if line == line[::-1]:
    print('YES')
else:
    print('NO')
