from random import randint
print('Sou seu computador...')

computer = randint(0, 10)

print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')

player = int(input('Qual é seu palpite? '))

tentativas = 1

while player != computer:
    if player < computer:
        print('Mais... Tente mais uma vez.')
        player = int(input('Qual é seu palpite? '))
        tentativas += 1
    elif player > computer:
        print('Menos... Tente mais uma vez.')
        player = int(input('Qual é seu palpite? '))
        tentativas += 1

print(f'Acertou com {tentativas} tentativas. Parabéns!')
