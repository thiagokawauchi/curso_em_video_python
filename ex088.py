from time import sleep
from random import randint
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
quantos_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{" SORTEANDO " + str(quantos_jogos) + " JOGOS ":=^40}')
for c in range(1, quantos_jogos + 1):
    print(f'JOGO {c}: ', end='')
    matriz = []
    for pos in range(0, 6):
        while True:
            number = randint(1, 60)
            if number not in matriz:
                matriz.append(number)
                break
    matriz.sort()
    print(matriz)
    matriz.clear()
    sleep(1)
print(f'{" < BOA SORTE! > ":=^40}')
