porridge: list[str] = ['Манная', 'Гречневая',
                       'Пшённая', 'Овсяная', 'Рисовая']

days: list[str] = [porridge[i % 5] for i in range(int(input()))]

for porridge_type in days:
    print(porridge_type)
