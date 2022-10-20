from datetime import date
cadastro = {}
cadastro['nome'] = str(input('Nome: ')).strip().title()
cadastro['idade'] = date.today().year - int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = ((cadastro['contratacao'] + 35) - date.today().year) + cadastro['idade']
print('-=-' * 20)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
