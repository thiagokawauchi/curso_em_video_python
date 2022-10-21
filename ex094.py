cadastros = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    cadastros.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
soma_idade = 0
for pes in cadastros:
    soma_idade += pes['idade']
media_idade = soma_idade / len(cadastros)
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pes in cadastros:
    if pes['sexo'] == 'F':
        print(f'{pes["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for pes in cadastros:
    if pes['idade'] > media_idade:
        for k, v in pes.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
