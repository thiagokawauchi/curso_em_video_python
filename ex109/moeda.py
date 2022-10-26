def aumentar(price=0, percent=0, formatar=False):
    resultado = price + (price * (percent / 100))
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def diminuir(price=0, percent=0, formatar=False):
    resultado = price - (price * (percent / 100))
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def dobro(price=0, formatar=False):
    resultado = price * 2
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def metade(price=0, formatar=False):
    resultado = price / 2
    if formatar:
        return moeda(resultado)
    else:
        return resultado


def moeda(price=0, moeda='R$'):
    resultado = f'R${price:.2f}'.replace('.', ',')
    return resultado
