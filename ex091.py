'''
from random import (randint)
from time import sleep
from operator import itemgetter
jogadores = {}
print('Valores sorteados: ')
for c in range(1, 5):
    dado = randint(1, 6)
    jogadores[f'jogador{c}'] = dado
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-=-' * 20)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
'''

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print('Valores sorteados: ')
for c in range(1, 5):
    dado = randint(1, 6)
    jogadores[f'jogador{c}'] = dado
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-=-' * 20)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(1)
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
