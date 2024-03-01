report: list[str] = []
while line := input():
    comm: int = line.find(' # ')
    if line.startswith('#'):
        continue

    line: str = line[:comm]
    report.append(line)

print('\n'.join(report))
