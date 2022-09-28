'''
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
'''

from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f'A hipotenusa vai medir {hipotenusa:.2f}.')
