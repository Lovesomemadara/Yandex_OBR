report: list[str, ...] = []
while line := input():
    if line.endswith('@@@'):
        continue
    elif line.startswith('##'):
        line = line[2:]
        report.append(line)
    else:
        report.append(line)

for word in report:
    print(word)
