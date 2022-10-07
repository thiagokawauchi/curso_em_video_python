print(f'{" LOJAS KAWAUCHI ":=^40}')

price = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

option = int(input('Qual é a opção? '))
if option == 1:
    print(f'Sua compra de R${price:.2f} vai custar R${price * 0.90:.2f} no final.')
elif option == 2:
    print(f'Sua compra de R${price:.2f} vai custar R${price * 0.95:.2f} no final')
elif option == 3:
    print(f'Sua compra será parcelada em 2x de R${price / 2:.2f} SEM JUROS.')
elif option == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${price * 1.20 / parcelas:.2f} COM JUROS.')
    print(f'Sua compra de R${price:.2f} vai custar {price * 1.20:.2f} no final.')
else:
    print('Opção inválida. Tente novamente.')
