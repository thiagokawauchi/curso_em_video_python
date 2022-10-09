frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
invertido = ''
for letter in range(len(frase) - 1, -1, -1):
    invertido += (frase[letter])
print(f'O inverso de {frase} é {invertido}')
if frase == invertido:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
