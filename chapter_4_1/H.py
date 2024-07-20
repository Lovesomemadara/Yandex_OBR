def is_palindrome(line):
    if isinstance(line, int):
        return str(line) == str(line)[::-1]
    else:
        return line == line[::-1]


# result = is_palindrome([1, 2, 1, 2, 1])
# print(f'result = {result}')
