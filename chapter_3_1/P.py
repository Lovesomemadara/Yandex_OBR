header_length: int = int(input())
header_count: list[str] = [input() for _ in range(int(input()))]

title = ''.join(header_count).strip()

shortened_title: str = ''

if len(title) <= header_length:
    print(title)
else:
    shortened_title = title[:header_length - 3] + '...'
    print(shortened_title)
