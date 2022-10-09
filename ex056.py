total_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
mulher_menor_20 = 0

for c in range(1, 5):
    print(f'{" " + str(c) + "ª Pessoa ":-^30}')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    total_idade += idade
    if sexo == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_menor_20 += 1

print(f'A média de idade do grupo é de {total_idade / 4:.1f} anos.')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {mulher_menor_20} mulheres com menos de 20 anos.')
