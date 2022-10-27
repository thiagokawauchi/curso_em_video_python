import moeda
price = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(price)} é {moeda.moeda(moeda.metade(price))}')
print(f'O dobro de {moeda.moeda(price)} é {moeda.moeda(moeda.dobro(price))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(price, 10))}')
