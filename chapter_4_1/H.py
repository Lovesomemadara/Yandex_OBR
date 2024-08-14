# №1
def is_palindrome(line: list | int | str | tuple) -> bool:
    if isinstance(line, int):
        line = str(line)
        return line == line[::-1]
    else:
        return line == line[::-1]


# №2
def is_palindrome(sequence: list | int | str | tuple) -> bool:
    if isinstance(sequence, int):
        notation: int = 10
        original: int = sequence

        total: int = 0
        while sequence > 0:
            last_digit: int = sequence % notation
            # ВАЖНО: Здесь не использовать оператор *=
            total = total * notation + last_digit
            sequence //= notation
        return total == original

    left: int = 0
    right: int = len(sequence) - 1
    while left < right:
        if sequence[left] != sequence[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome([1, 2, 2, 1]))
print(is_palindrome(123121))
print(is_palindrome(123321))
print(is_palindrome('abba'))
