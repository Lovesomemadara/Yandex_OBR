# set - множество

# unique: set[int] = {3, 1, 2, 10, 44, 6}
# print(unique)
#
# # -------------
#
# text: str = 'Hello, WorLd!'
#
# print(set(text))
# Array = [10, 20, 50, 40, 30]
# Map = {"a", "b"}
#
# print(
#     {[1, 2, 3], [10, 20]}
# )

# ------------------------

# data: dict[str, int] = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "один": 1,
#     "два": 2,
#     "три": 3,
# }
#
# print(data)

# info: dict[str, str] = {
#     "sep": "\n\n"
# }
#
# print(**info)


# ключ1: значение,
# ключ2: значение,
# ключ3: значение1,

# unique_nums: set[int] = set()
#
# for _ in range(5):
#     unique_nums.add(
#         int(input())
#     )
#
# print(unique_nums)

data: dict[int | str, str] = {}
# data = dict()

# for i in range(1, 4):
#     data[i] = input()

data["user"] = "Admin"
data["password"] = "1234"

# print(data)
# print(data["user"])
# print(data["user2"])  # KeyError
# print(data.get("user2", -1))

# print(data.keys())
# dict_keys(
#     ['user', 'password']
# )
#
# print(data.values())
# dict_values(
#     ['Admin', '1234']
# )
#
# print(data.items())
# dict_items(
#     [
#         ('user', 'Admin'),
#         ('password', '1234')
#     ]
# )

# if "some" in data:
#     pass

# for elem in data:
# for elem in data.keys():
#     print(elem)


# for elem in data.values():
#     print(elem)


# for item in data.items():
#     first, second = item
#     print(f"Ключ: {first} - Значение: {second}")
#
# for first, second in data.items():
#     print(f"Ключ: {first} - Значение: {second}")
#
# for key, value in data.items():
#     print(f"Ключ: {key} - Значение: {value}")

# get("Ключ")
# get("Ключ", "Значение, если такого ключа нет")

# keys()
# values()
# items()


# res = data.pop("user")
# print(res)
# print(data)


# print(data.popitem())
# print(data)

# Словарь - Хеш-таблицы - HashMap


text: str = 'Hello, WorLd!'

counter: dict[str, int] = {}
for char in set(text):
    counter[char] = text.count(char)
print(counter)

text: str = 'Привет, Мир!'
counter: dict[str, int] = {}

for char in text:
    if char in counter:
        counter[char] = counter[char] + 1
        # counter[char] += 1
    else:
        counter[char] = 1
    # counter[char] = counter.get(char, 0) + 1

print(counter)
