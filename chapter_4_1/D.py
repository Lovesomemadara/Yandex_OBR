def month(num: int, lang: str) -> str:
    months_ru: list[str] = ['Январь', 'Февраль', 'Март',
                            'Апрель', 'Май', 'Июнь',
                            'Июль', 'Август', 'Сентябрь',
                            'Октябрь', 'Ноябрь', 'Декабрь']
    months_en: list[str] = ['January', 'February', 'March',
                            'April', 'May', 'June',
                            'July', 'August', 'September',
                            'October', 'November', 'December']
    if lang == "ru":
        return months_ru[num - 1]
    else:
        return months_en[num - 1]


# result = month(3, "en")
# print(result)
