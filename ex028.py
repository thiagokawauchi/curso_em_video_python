from random import randint
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
computer_number = randint(0, 5)
print('\033[33m-=-\033[m' * 20)
player_number = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if computer_number == player_number:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[31mGANHEI! Eu pensei no número {computer_number} e não no {player_number}!\033[m')
