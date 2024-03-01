sentenses = [input() for _ in range(int(input()))]
find_word: str = input().lower()

for sentense in sentenses:
    if sentense.lower().find(find_word) != -1:
        print(''.join(sentense))
