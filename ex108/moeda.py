def aumentar(price=0, percent=0):
    resultado = price + (price * (percent / 100))
    return resultado


def diminuir(price=0, percent=0):
    resultado = price - (price * (percent / 100))
    return resultado


def dobro(price=0):
    resultado = price * 2
    return resultado


def metade(price=0):
    resultado = price / 2
    return resultado


def moeda(price=0, moeda='R$'):
    resultado = f'R${price:.2f}'.replace('.', ',')
    return resultado
