salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    salario_atualizado = salario * 1.15
else:
    salario_atualizado = salario * 1.10

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_atualizado:.2f} agora.')
