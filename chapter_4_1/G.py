def can_eat(knight, piece):
    dx = abs(knight[0] - piece[0])
    dy = abs(knight[1] - piece[1])
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


# result = can_eat((2, 1), (4, 2))
# print(f'result = {result}')
