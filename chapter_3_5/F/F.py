TRANSCRIPTION: dict[str, str] = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
}

with (open('transliteration.txt', mode='w', encoding='UTF-8') as file_out,
      open('cyrillic.txt', mode='r', encoding='UTF-8') as file_in):
    transliteration_frase: str = ''
    for line in file_in:
        for char in line:
            char_copy: str = char.upper()
            if char_copy in TRANSCRIPTION:
                if char.isupper():
                    char: str = TRANSCRIPTION[char_copy].capitalize()
                else:
                    char: str = TRANSCRIPTION[char_copy].lower()
            transliteration_frase += char

    file_out.writelines(transliteration_frase)
