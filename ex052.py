number = int(input('Digite um número: '))

soma_divisivel = 0

for c in range(1, number + 1):
    if number % c == 0:
        print(f'\033[1:33m{c}\033[m', end=' ')
        soma_divisivel += 1
    else:
        print(f'\033[1:31m{c}\033[m', end=' ')

print(f'\nO número {number} foi divisível {soma_divisivel} vezes.')

if soma_divisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
