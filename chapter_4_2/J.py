def secret_replace(text, **replaces):
    for old, new in replaces.items():
        for replacement in new:
            text = text.replace(old, replacement)
    return text


result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
print(result)
