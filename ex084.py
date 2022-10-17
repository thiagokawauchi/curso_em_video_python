pessoas = []
dado = []
maior = menor = 0
maior_pessoa = []
menor_pessoa = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    if dado[1] > maior:
        maior = dado[1]
    if menor == 0 or dado[1] < menor:
        menor = dado[1]
    dado.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Opção inválida. Digite novamente.')
    if continuar == 'N':
        break
total_pessoas = len(pessoas)
for p in pessoas:
    if p[1] == maior:
        maior_pessoa.append(p[0])
    if p[1] == menor:
        menor_pessoa.append(p[0])
print('-=-' * 20)
print(f'Ao todo você cadastrou {total_pessoas} pessoas.')
print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for heavy_people in maior_pessoa:
    print(f'{heavy_people} ', end='')
print(f'\nO menor peso foi de {menor:.1f}kg. Peso de ', end='')
for light_people in menor_pessoa:
    print(f'{light_people} ', end='')
