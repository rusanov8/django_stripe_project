
def convert_value(amount, currency):
    """
        Конвертирует значение из доллара в рубли.
    """

    USD_RATE = 90

    if currency == 'RUB':
        return amount
    else:
        return amount * USD_RATE