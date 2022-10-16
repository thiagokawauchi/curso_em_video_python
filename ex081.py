lista = []
while True:
    number = int(input('Digite um valor: '))
    lista.append(number)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Opção inválida. Digite novamente.')
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
