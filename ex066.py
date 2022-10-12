soma = vezes = 0
while True:
    number = int(input('Digite um valor (999 para parar): '))
    if number == 999:
        break
    soma += number
    vezes += 1
print(f'A soma dos {vezes} valores foi {soma}!')
