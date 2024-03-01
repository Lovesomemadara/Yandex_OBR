report: list[str] = []
tag = '#'

while line := input():
    if tag in line:
        line = line[:line.find(tag)]
    line = line.rstrip()

    if line:
        report.append(line)

print('\n'.join(report))
