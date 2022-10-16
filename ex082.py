lista_completa = []
lista_pares = []
lista_impares = []
while True:
    lista_completa.append(int(input('Digite um número: ')))
    if lista_completa[-1] % 2 == 0:
        lista_pares.append(lista_completa[-1])
    else:
        lista_impares.append(lista_completa[-1])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Opção inválida. Digite novamente.')
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'A lista completa é {lista_completa}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')
