from itertools import count

start, end, step = map(float, input().split())

for value in count(start, step):
    if value <= end:
        print('{:.2f}'.format(round(value, 2)))
    else:
        break
