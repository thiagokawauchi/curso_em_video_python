total_maior_18 = total_homens = mulher_menor_20 = 0
while True:
    print('-' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total_maior_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_maior_18}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {mulher_menor_20} mulheres com menos de 20 anos')
