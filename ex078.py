valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('-=-' * 12)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, valor, in enumerate(valores):
    if valor == max(valores):
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{i}... ', end='')
