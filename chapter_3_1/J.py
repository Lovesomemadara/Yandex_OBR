# Логика задачи: Все вводимые текстовые строки собрать в одну переменную.

all_lines: str = ''
while (line := input()) != 'ФИНИШ':
    all_lines += line.rstrip()
all_lines = all_lines.replace(' ', '').lower()

# Используя множество берутся только уникальные символы строки
# unique_letters: set = set(all_lines)  # эту переменную не буду хранить
# в памяти, сразу передам в итератор

frequency_chars: list[str] = []
max_count: int = 0
# for letter in unique_letters:
for letter in set(all_lines):
    # Подсчитывается количество символов в строке и записывается
    # в переменную temp. Проверка должна быть обязательна
    # в два этапа (не использовать >=), чтобы по частоте одинаковые
    # символы добавлялись в список, а если найден элемент самый частотный,
    # то очищается список и туда добавляется элемент.

    # Подобную задачу Вы решали, вот ссылка:
    # https://github.com/Lovesomemadara/topic_9/blob/main/tasks/part_2_insightful/task_8.py

    if (temp := all_lines.count(letter)) > max_count:
        max_count = temp
        frequency_chars.clear()
        frequency_chars.append(letter)

    elif temp == max_count:
        frequency_chars.append(letter)

frequency_chars.sort()
print(frequency_chars[0])
