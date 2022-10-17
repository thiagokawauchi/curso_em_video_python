matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for primeira_camada, n1 in enumerate(matriz):
    for segunda_camada, n2 in enumerate(matriz[primeira_camada]):
        matriz[primeira_camada][segunda_camada] = int(input(f'Digite um valor para [{primeira_camada}, {segunda_camada}]: '))
print('-=-' * 20)
for primeira_camada, n1 in enumerate(matriz):
    for segunda_camada, n2 in enumerate(matriz[primeira_camada]):
        print(f'[{matriz[primeira_camada][segunda_camada]:^5}] ', end='')
    print()
