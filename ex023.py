'''
num = str(input('Digite um número: ')).strip()
print(f'Analisando o número {num}')
print(f'Unidade: {num[len(num) - 1 : ]}')
print(f'Dezena: {num[len(num) - 2 : len(num) - 1]}')
print(f'Centena: {num[len(num) - 3 : len(num) - 2]}')
print(f'Milhar: {num[len(num) - 4 : len(num) - 3]}')
'''

num = int(input('Digite um número: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
