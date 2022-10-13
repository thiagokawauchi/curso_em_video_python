from random import randint
tupla = ()
print('Os valores sorteados foram: ', end='')
for c in range(0, 5):
    random_number = randint(0, 10)
    random_tuple = (random_number,)
    print(f'{random_number} ', end='')
    tupla += random_tuple
maior = 0
menor = 0
for c in range(0, 5):
    if tupla[c] > maior:
        maior = tupla[c]
    if c == 0 or tupla[c] < menor:
        menor = tupla[c]
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print(f'Max: {max(tupla)}')
print(f'Min: {min(tupla)}')
