print('=' * 40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('=' * 40)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(termo, termo + (razao * 10), razao):
    print(f'{c} →', end=' ')
print('ACABOU')