# Solução com For Loop
''''
number = int(input('Digite um número para \ncalcular seu Fatorial: '))
fatorial = 1
resultado = f'Calculando {number}! = '
for i in range(number, 0, -1):
    fatorial *= i
    if i != 1:
        resultado += f'{i} x '
    else:
        resultado += f'{i} = '
fatorial_str = str(fatorial)
print(resultado + fatorial_str)
'''

# Solução com While Loop

number = int(input('Digite um número para \ncalcular seu Fatorial: '))
counter = number
fatorial = 1
resultado = f'Calculando {number}! = '
while counter != 0:
    fatorial *= counter
    if counter != 1:
        resultado += f'{counter} x '
    else:
        resultado += f'{counter} = '
    counter -= 1
print(f'{resultado}{fatorial}')
