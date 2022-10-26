import moeda
price = float(input('Digite o preço: R$'))
print(f'A metade de R${price} é R${moeda.metade(price)}')
print(f'O dobro de R${price} é R${moeda.dobro(price)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(price)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(price)}')
