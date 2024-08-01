print(*filter(lambda x: sum(map(int, str(x))) % 2 == 0, (1, 2, 3, 4, 5)))

print(*filter(lambda x: sum(map(int, str(x))) % 2 == 0, (32, 64, 128, 256, 512)))
