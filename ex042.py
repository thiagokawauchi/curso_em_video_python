seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg2 + seg3:
    if seg1 == seg2 == seg3:
        tipo = 'EQUILÁTERO'
    elif seg1 == seg2 or seg2 == seg3 or seg3 == seg1:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo}!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
