print('-' * 40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
total = greater_1000 = cheaper = 0
cheaper_name = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().title()
    price = float(input('Preço: R$'))
    total += price
    if price > 1000:
        greater_1000 += 1
    if cheaper == 0 or price < cheaper:
        cheaper = price
        cheaper_name = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {greater_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheaper_name} que custa R${cheaper:.2f}')
