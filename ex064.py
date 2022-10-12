number = 0
soma = 0
quantidade = 0
while number != 999:
    number = int(input('Digite um número [999 para parar]: '))
    if number != 999:
        soma += number
        quantidade += 1
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}.')
