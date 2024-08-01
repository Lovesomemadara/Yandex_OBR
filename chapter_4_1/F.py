base: set[str] = set()


def modern_print(line: str) -> str:
    if line not in base:
        print(line)
        base.add(line)


modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
