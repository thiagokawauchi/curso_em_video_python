medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida:.1f}m corresponde a:')
print(f'{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')
