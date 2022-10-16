lista = []
while True:
    number = int(input('Digite um valor: '))
    if number not in lista:
        lista.append(number)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=-' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')
