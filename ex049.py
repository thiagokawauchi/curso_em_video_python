number = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{number} x {c:2} = {number * c}')
