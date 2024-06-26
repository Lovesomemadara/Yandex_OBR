stack: list[int] = []

for i in input().split(' '):
    if not i.isdigit():
        if i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif i == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(a + b)
    else:
        stack.append(int(i))

print(*stack)
