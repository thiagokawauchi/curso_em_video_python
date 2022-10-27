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


def resumo(price, increase_tax=10, decrease_tax=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(price)}')
    print(f'{"Dobro do preço:":<20}{dobro(price, True)}')
    print(f'{"Metade do preço:":<20}{metade(price, True)}')
    print(f'{str(increase_tax) + "%":<5}{"de aumento:":<15}{aumentar(price, increase_tax, True)}')
    print(f'{str(decrease_tax) + "%":<5}{"de redução:":<15}{diminuir(price, decrease_tax, True)}')
    print('-' * 30)
