option = ''
vezes = soma = maior = menor = 0
while option != 'N':
    number = int(input('Digite um número: '))
    vezes += 1
    soma += number
    if number > maior:
        maior = number
    if menor == 0 or number < menor:
        menor = number
    option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while option != 'N' and option != 'S':
        print('Opção inválida. Digite novamente.')
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / vezes
print(f'Você digitou {vezes} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
