velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h.')
    print(f'\033[31mVocê deve pagar uma multa de R${(velocidade - 80) * 7:.2f}!\033[m')
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
