def calcule_area(larg, comp):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area:.1f}m².')


print(f'{"Controle de Terrenos":^20}')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcule_area(largura, comprimento)
