def aumentar(price, percent=10):
    resultado = price + (price * (percent / 100))
    return resultado


def diminuir(price, percent=10):
    resultado = price - (price * (percent / 100))
    return resultado


def dobro(price):
    resultado = price * 2
    return resultado


def metade(price):
    resultado = price / 2
    return resultado
