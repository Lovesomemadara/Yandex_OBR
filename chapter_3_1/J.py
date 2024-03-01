count = [0] * 33
max_char = ''
max_count = 0

while (line := input()) != 'ФИНИШ':
    for char in line:
        if char.isalpha():
            char = char.lower()
            index = ord(char) - ord('а')
            count[index] += 1
            if count[index] > max_count:
                max_char = char
                max_count = count[index]

print(max_char.lower())
