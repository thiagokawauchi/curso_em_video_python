'''

# Primeira solução

lista = []
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
lista.append(n1)
lista.append(n2)
lista.append(n3)
print(f'O menor valor digitado foi {min(lista)}')
print(f'O maior valor digitado foi {max(lista)}')
'''

'''

# Segunda solução

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

if n1 < n2 and n1 < n3:
    print(f'O menor valor digitado foi {n1}')
elif n2 < n3 and n2 < n1:
    print(f'O menor valor digitado foi {n2}')
else:
    print(f'O menor valor digitado foi {n3}')

if n1 > n2 and n1 > n3:
    print(f'O maior valor digitado foi {n1}')
elif n2 > n3 and n2 > n1:
    print(f'O maior valor digitado foi {n2}')
else:
    print(f'O maio valor digitado foi {n3}')
'''

# Solução Guanabara

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
