print('Gerador de PA ver. Super')
print('-=-' * 6)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
counter = 1
mais_termos = 10
total = mais_termos
while mais_termos != 0:
    while counter <= total:
        print(f'{termo} → ', end='')
        termo += razao
        counter += 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? (0 para encerrar) '))
    total += mais_termos
print(f'Progressão finalizada com {total} termos mostrados.')
