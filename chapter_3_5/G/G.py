with open(input(), mode='r', encoding='UTF-8') as file_in:
    numbers: list[int] = [int(number) for number in file_in.read().split()]

print(length := len(numbers))
print(len([number for number in numbers if number > 0]))
print(min(numbers))
print(max(numbers))
print(total := sum(numbers))
print(round(total / length, 2))
