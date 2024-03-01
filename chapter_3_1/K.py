sentenses = [input() for _ in range(int(input()))]
find_word: str = input().lower()

for sentense in sentenses:
    if find_word in sentense.lower():
        print(sentense)
