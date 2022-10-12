from random import randint
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
count = 0
while True:
    print('-=-' * 10)
    player = int(input('Diga um valor: '))
    par_ou_impar = ' '
    while par_ou_impar not in 'PI':
        par_ou_impar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if par_ou_impar == 'I':
        par_ou_impar = 'Í'
    print('-' * 30)
    computer = randint(1, 10)
    soma = player + computer
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {player} e o computador {computer}. Total de {soma} deu {resultado}')
    print('-' * 30)
    if par_ou_impar == resultado[0]:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
    else:
        print('Você PERDEU!')
        break
print('-=-' * 10)
print(f'GAME OVER! Você venceu {count} vezes.')
