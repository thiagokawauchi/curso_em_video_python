dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${total:.2f}.')
