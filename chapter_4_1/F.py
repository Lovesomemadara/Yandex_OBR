base: set[str] = set()


# №1
def modern_print(line: str) -> str:
    if line not in base:
        print(line)
        base.add(line)


# №2
# А можно передать список в качестве аргумента по умолчанию.
# Вместо глобальной переменной.
def modern_print(line: str, seen_data: list = []):
    if line not in seen_data:
        seen_data.append(line)
        print(line)


modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")
