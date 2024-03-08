header_length: int = int(input())
header_count: list[str] = [input() for _ in range(int(input()))]

title = ''.join(header_count).strip()

shortened_title: str = ''

if len(title) <= header_length:
    print(title)
else:
    shortened_title = title[:header_length - 3] + '...'
    print(shortened_title)

"""
length: int = int(input())  # L — необходимая длина заголовка
n: int = int(input())  # N — количество строк в заголовке новости

title: str = ""
for i in range(n):  # N строк записано по одной строке заголовка.
    title += input()
    if i != n - 1:
        title += "\n"

title_length = len(title)

slash_n_count = title.count('\n')
dots: str = "..."
if (title_length - slash_n_count) > length:
    slash_n_count = title[:length - 3].count('\n')
    title = title[:length - 3 + slash_n_count] + dots

    # ...

    print(title)
else:
    print(title)
"""
