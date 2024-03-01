porridge: list[str] = ['Манная', 'Гречневая',
                       'Пшённая', 'Овсяная', 'Рисовая']

days: list[str] = [porridge[i % len(porridge)] for i in range(int(input()))]

for porridge_type in days:
    print(porridge_type)
