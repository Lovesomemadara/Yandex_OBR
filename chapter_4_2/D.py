def month(num: int, lang: str = 'ru') -> str:
    # TODO: Здесь лучше использовать словарь.
    languages: dict[str, dict[int, str]] = {
        'en': {
            0: 'january',
            1: 'february',
        },
        'ru': {
            0: 'январь',
            1: 'февраль',
        }
    }

    # months_ru: list[str] = ['Январь', 'Февраль', 'Март',
    #                         'Апрель', 'Май', 'Июнь',
    #                         'Июль', 'Август', 'Сентябрь',
    #                         'Октябрь', 'Ноябрь', 'Декабрь']
    # months_en: list[str] = ['January', 'February', 'March',
    #                         'April', 'May', 'June',
    #                         'July', 'August', 'September',
    #                         'October', 'November', 'December']
    # if lang == 'en':
    #     return months_en[num - 1]
    # else:
    #     return months_ru[num - 1]
    return languages.get(lang).get(num - 1).capitalize()


result = month(2)
print(f'result = {result}')
