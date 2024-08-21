from sys import stdin

*lines, query = [x.strip() for x in stdin.readlines()]

for line in lines:
    if line.lower().find(query.lower()) + 1:
        print(line)
