nome_completo = str(input('Digite seu nome completo: ')).strip().title().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome_completo[0]}')
print(f'Seu último nome é {nome_completo[len(nome_completo) - 1]}')
