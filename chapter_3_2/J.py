transliterator: dict[str, str] = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}

trans_frase: str = ''
for char in input():
    if char.isalpha():
        if char.upper() not in transliterator:
            trans_frase += ''
        else:
            if char.isupper():
                trans_frase += transliterator.get(char.upper(), char).capitalize()
            else:
                trans_frase += transliterator.get(char.upper(), char).lower()
    else:
        trans_frase += char
print(trans_frase)
