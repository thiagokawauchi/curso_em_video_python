from time import sleep
from random import randint
numeros = []


def sorteia():
    print('Sorteando os valores da lista: ', end='')
    for i in range(0, 5):
        sleep(0.5)
        number = randint(1, 10)
        print(number, end=' ')
        numeros.append(number)
    sleep(0.5)
    print('PRONTO!')
    sleep(0.5)


def somaPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')


sorteia()
somaPar()
