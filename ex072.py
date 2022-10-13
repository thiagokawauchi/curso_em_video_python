tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        number = int(input('Digite um número entre 0 e 20: '))
        if number >= 0 and number <= 20:
            break
        else:
            print('Tente novamente.', end=' ')
    print(f'Você digitou o número {tupla[number]}')
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('FIM')
