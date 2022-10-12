print('=' * 40)
print(f'{"BANCO CEV":^40}')
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
while True:
    cedulas_50 = valor // 50
    valor -= cedulas_50 * 50
    print(f'Total de {cedulas_50} cédulas de R$50')
    if valor == 0:
        break
    cedulas_20 = valor // 20
    valor -= cedulas_20 * 20
    print(f'Total de {cedulas_20} cédulas de R$20')
    if valor == 0:
        break
    cedulas_10 = valor // 10
    valor -= cedulas_10 * 10
    print(f'Total de {cedulas_10} cédulas de R$10')
    if valor == 0:
        break
    cedulas_1 = valor // 1
    valor -= cedulas_1 * 1
    print(f'Total de {cedulas_1} cédulas de R$1')
    if valor == 0:
        break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
