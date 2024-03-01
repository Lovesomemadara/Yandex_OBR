header_length: int = int(input())
headers = [input() for _ in range(int(input()))]

for header in headers:
    if len(header) > header_length:
        print(f'{header[:header_length - 3]}...')
    else:
        print(header)
