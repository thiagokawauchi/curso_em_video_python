def fatorial(number=1, show=False):
    '''
    -> Calcula o Fatorial de um número.
    :param number: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número number
    '''
    print('-' * 30)
    f = 1
    for i in range(number, 0, -1):
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
        f *= i
    return f


help(fatorial)
print(fatorial(5, True))
