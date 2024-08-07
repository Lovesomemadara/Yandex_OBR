def make_equation(*args) -> str:
    if len(args) == 1:
        return args[0]
    else:
        return f'({make_equation(*args[:-1])}) * x + {args[-1]}'


if __name__ == '__main__':
    print(make_equation(3, 2, 1))
