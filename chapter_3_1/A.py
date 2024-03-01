words = [input() for _ in range(int(input()))]
CHECKING_CHARS: tuple[str, ...] = ('а', 'б', 'в')

for word in words:
    if not word.lower().startswith(CHECKING_CHARS):
        print('NO')
        break
else:
    print('YES')
