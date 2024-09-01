def secret_replace(text: str, **kwargs) -> str:
    new_text: str = ''
    kwargs: dict[str, list] = {
        key: [value, 0]
        for key, value in kwargs.items()
    }
    for char in text:
        if char in kwargs:
            pos: int = kwargs[char][1] % len(kwargs[char][0])
            new_text += kwargs[char][0][pos]
            kwargs[char] = [kwargs[char][0], pos + 1]
        else:
            new_text += char

    return new_text


print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))


# №2

def replace_string(text: str, sub: str, values: tuple[str]) -> str:
    length: int = len(values)
    i: int = 0
    while sub in text:
        text = text.replace(sub, values[i], 1)
        i += 1
        i %= length

    return text


def secret_replace(text: str, **replaces) -> str:
    """Позволит быстро шифровать сообщения.

    :param text: Текст требующий шифрования.
    :param replaces: Именованные аргументы - правила замен.
    Представляющие собой кортежи из одного или нескольких значений.
    """

    for key, values in replaces.items():
        text = replace_string(text, key, values)

    return text
