lista = ()
for c in range(1, 5):
    number = (int(input(f'Digite o {c}º valor: ')),)
    lista += number
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
pares = 0
for par in lista:
    if par % 2 == 0:
        pares += 1
print(f'Os valores pares foram digitados {pares} vezes')
