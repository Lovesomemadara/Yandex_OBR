def is_palindrome(line: list | int) -> bool:
    if isinstance(line, int):
        return str(line) == str(line)[::-1]
    else:
        return line == line[::-1]


print(is_palindrome([1, 2, 1, 2, 1]))
