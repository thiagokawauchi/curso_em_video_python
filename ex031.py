distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}km.')
if distancia <= 200:
    print(f'E o preço da sua passagem será de R${distancia * 0.50:.2f}.')
else:
    print(f'E o preço da sua passagem será de R${distancia * 0.45:.2f}')
