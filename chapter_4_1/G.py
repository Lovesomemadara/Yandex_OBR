def can_eat(knight: tuple[int, int], piece: tuple[int, int]) -> bool:
    dx: int = abs(knight[0] - piece[0])
    dy: int = abs(knight[1] - piece[1])
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


print(can_eat((2, 1), (4, 2)))
