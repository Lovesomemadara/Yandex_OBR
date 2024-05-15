tokens: list[str] = input().split()

uno: str = '~#!'
duo: str = '+-*/'
trio: str = '@'

stack: list[int] = []

while tokens:
    token = tokens.pop(0)
    if token in uno:
        a: int = stack.pop()
        match token:
            case '~':
                stack.append(-a)
            case '!':
                res: int = 1
                for i in range(1, a + 1):
                    res *= i
                stack.append(res)
            case '#':
                stack.append(a)
                stack.append(a)
    elif token in duo:
        a: int = stack.pop()
        b: int = stack.pop()
        match token:
            case '+':
                stack.append(b + a)
            case '-':
                stack.append(b - a)
            case '*':
                stack.append(b * a)
            case '/':
                stack.append(b // a)
    elif token in trio:
        a: int = stack.pop()
        b: int = stack.pop()
        c: int = stack.pop()
        stack.append(b)
        stack.append(a)
        stack.append(c)
    else:
        stack.append(int(token))

print(int(stack[0]))
