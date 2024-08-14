# 1. Встроенние модули
import os
import time
# from math import *
from random import choices, randint
from sys import stdin, stdout
from datetime import datetime as dt

# 2. Внешние модули
import requests

# 3. Модули проекта
from examples.algebra.math import custom_pow
from examples.modules.file_1 import PI
# from .file_1 import PI


# print(custom_pow(2, 6))
# print(PI)


# ------------------

# os.mkdir('test')

# print(dt.now().strftime('%d-%m-%Y'))

# ------------------

# def ranger(start, end):
#     result = []
#
#     for i in range(start, end):
#         result.append(i)
#
#
# start_time = time.time()
# ranger(1, 100000000)
# end_time = time.time()
# res = end_time - start_time
# print(f"Функции выполнилась {res:.4f} сек.")
# ------------------


print(randint(10, 100))
print(choices(range(10, 100), k=25))

url = requests.get('https://google.com')
print(url.text)
