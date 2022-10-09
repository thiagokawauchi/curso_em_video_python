maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso

print(f'O maior peso lido foi de {maior:.1f}kg')
print(f'O menor peso lido foi de {menor:.1f}kg')
