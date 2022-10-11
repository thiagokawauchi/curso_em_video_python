print('Gerador de PA')
print('-=-' * 6)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print(f'{termo} → ', end='')
counter = 1
while counter < 10:
    print(f'{termo + (razao * counter)} → ', end='')
    counter += 1
print('FIM')
