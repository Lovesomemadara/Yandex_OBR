base: set[str] = set()


def modern_print(line):
    if line not in base:
        print(line)
        base.add(line)
