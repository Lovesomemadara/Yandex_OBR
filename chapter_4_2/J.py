def secret_replace(text: str, **kwargs) -> str:
    new_text: str = ''
    kwargs: dict[str, ...] = {key: [value, 0] for key, value in kwargs.items()}
    for char in text:
        if char in kwargs:
            pos: int = kwargs[char][1] % len(kwargs[char][0])
            new_text += kwargs[char][0][pos]
            kwargs[char] = [kwargs[char][0], pos + 1]
        else:
            new_text += char

    return new_text


print(secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z")))
