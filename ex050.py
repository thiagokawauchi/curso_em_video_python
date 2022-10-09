contador = 0
soma = 0
for c in range(1, 7):
    number = int(input(f'{c}º número inteiro: '))
    if number % 2 == 0:
        soma += number
        contador += 1
print(f'Você informou {contador} números pares, e a soma dos números pares é {soma}')
