from time import sleep
from random import randint
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

computer_number = randint(1, 3)
if computer_number == 1:
    computer_play = 'Pedra'
elif computer_number == 2:
    computer_play = 'Papel'
else:
    computer_play = 'Tesoura'

player_number = int(input('Qual é a sua jogada? '))
if player_number not in [1, 2, 3]:
    print('Opção inválida. Tente novamente.')
else:
    if player_number == 1:
        player_play = 'Pedra'
    elif player_number == 2:
        player_play = 'Papel'
    else:
        player_play = 'Tesoura'

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=-' * 8)
    print(f'Computador jogou {computer_play}')
    print(f'Jogador jogou {player_play}')
    print('-=-' * 8)

    if computer_number == player_number:
        print('DEU EMPATE')
    elif computer_number == 1 and player_number == 2:
        print('JOGADOR VENCE')
    elif computer_number == 1 and player_number == 3:
        print('COMPUTADOR VENCE')
    elif computer_number == 2 and player_number == 1:
        print('COMPUTADOR VENCE')
    elif computer_number == 2 and player_number == 3:
        print('JOGADOR VENCE')
    elif computer_number == 3 and player_number == 1:
        print('JOGADOR VENCE')
    elif computer_number == 3 and player_number == 2:
        print('COMPUTADOR VENCE')
