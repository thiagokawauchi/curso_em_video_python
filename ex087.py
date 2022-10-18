matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0
for c in range(0, 3):
    for pos, value in enumerate(matriz[c]):
        matriz[c][pos] = int(input(f'Digite um valor para [{c}, {pos}]: '))
        if matriz[c][pos] % 2 == 0:
            soma_pares += matriz[c][pos]
        if pos == 2:
            soma_terceira_coluna += matriz[c][pos]
        if c == 1:
            if pos == 0 or matriz[c][pos] > maior_segunda_linha:
                maior_segunda_linha = matriz[c][pos]
print('-=-' * 20)
for c in range(0, 3):
    for pos, value in enumerate(matriz[c]):
        print(f'[{matriz[c][pos]:^5}] ', end='')
    print()
print('-=-' * 20)
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {maior_segunda_linha}.')
