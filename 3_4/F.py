from itertools import product

RANKS: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
SUITS: list[str] = ['пик', 'треф', 'бубен', 'червей']

line: str = input()

cards: list[str] = [f'{rank} {suit}' for rank, suit in product(RANKS, SUITS) if suit != line]

for card in cards:
    print(card)
