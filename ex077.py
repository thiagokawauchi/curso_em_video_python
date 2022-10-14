palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    if palavras.index(palavra) == 0:
        print(f'Na palavra {palavra} temos', end=' ')
    else:
        print(f'\nNa palavra {palavra} temos', end=' ')
    for letter in palavra:
        if letter in 'AEIOU':
            print(letter.lower(), end=' ')
