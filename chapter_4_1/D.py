# №1
# def month(num: int, lang: str) -> str:
#     months_ru: list[str] = ['Январь', 'Февраль', 'Март',
#                             'Апрель', 'Май', 'Июнь',
#                             'Июль', 'Август', 'Сентябрь',
#                             'Октябрь', 'Ноябрь', 'Декабрь']
#     months_en: list[str] = ['January', 'February', 'March',
#                             'April', 'May', 'June',
#                             'July', 'August', 'September',
#                             'October', 'November', 'December']
#     if lang == 'ru':
#         return months_ru[num - 1]
#     else:
#         return months_en[num - 1]
#

# №2
# Предлагаю использовать словарь
def month(day: int, language: str) -> str | None:
    months: dict[str, dict[int, str]] = {
        'en': {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        },

        'ru': {
            1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь',
        },
    }
    if language == 'en':
        return months[language].get(day)
    elif language == 'ru':
        return months[language].get(day)


result = month(3, 'en')
print(result)
