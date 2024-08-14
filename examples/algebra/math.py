def custom_pow(num: int | float, exp: int | float) -> int | float:
    """Возведение в степень.
    :param num:
    :param exp:
    :return:
    """
    return num ** exp


if __name__ == '__main__':
    print(custom_pow(2, 5))
