"""
r - read
w - write
a - append
"""

from csv import reader
import json
from pprint import pprint
from random import choices


# ----------------------- r

def r():
    file = open('input.txt', mode='r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    print(data)

    # Контекстный менеджер
    with open('input.txt', mode='r', encoding='UTF-8') as file_r:
        print(file_r.readlines())


# ----------------------- w
def w():
    nums: list[int] = choices(range(100, 1000), k=150)

    w_file = open('data_1.txt', mode='w', encoding='UTF-8')
    w_file.writelines(
        map(lambda num: f'{num}\n', nums)
    )

    w_file.write(
        '\n'.join(map(str, nums))
    )

    w_file.close()


def a():
    with open('input.txt', mode='a', encoding='UTF-8') as file_a:
        file_a.write('101\n')


def sort_file_nums(filename: str, encoding='UTF-8'):
    with (open(filename, mode='r', encoding=encoding) as read,
          open('even_nums.txt', mode='w', encoding=encoding) as evens,
          open('odd_nums.txt', mode='w', encoding=encoding) as odds):
        nums = map(str.strip, read.readlines())
        e_nums = []
        o_nums = []
        [e_nums.append(f'{num}\n')
         if int(num) % 2 == 0
         else o_nums.append(f'{num}\n')
         for num in nums]
        evens.writelines(e_nums)
        odds.writelines(o_nums)


# sort_file_nums('input.txt')


# ------------------------------ json


def json_reader(filename: str, encoding='UTF-8'):
    with open(filename, mode='r', encoding=encoding) as file:
        return json.load(file)


print(json_reader('data.json'))

# try:
#     func('1', [5])
# except Exception as err:
#     print(f'Ура! Ошибка!, {err}')
# func('1', [5])
