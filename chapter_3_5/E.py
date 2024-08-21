from sys import stdin

palindrome_words: set[str] = set()

lines: list[str] = []

for line in stdin.readlines():
    lines.extend(line.strip().split())

for word in lines:
    if word.lower() == word.lower()[::-1]:
        palindrome_words.add(word)


print('\n'.join(sorted(palindrome_words)))
