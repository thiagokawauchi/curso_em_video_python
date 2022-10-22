from time import sleep


def contador(start, end, step):
    print('-=-' * 20)
    print(f'Contagem de {start} até {end} de {step} em {step}')
    sleep(1)
    if start > end:
        end -= 1
        if step > 0:
            step *= -1
        elif step == 0:
            step = -1
    elif start < end:
        end += 1
        if step < 0:
            step *= -1
        elif step == 0:
            step = 1
    for c in range(start, end, step):
        print(f'{c} ', end='')
        sleep(0.5)
    print('FIM!')
    sleep(0.5)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
