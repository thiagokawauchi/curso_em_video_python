numbers = [[], []]
for c in range(1, 8):
    number = int(input(f'Digite o {c}o. valor: '))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
print('-=-' * 20)
numbers[0].sort()
numbers[1].sort()
print(f'Os valores pares digitados foram: {numbers[0]}')
print(f'Os valores ímpares digitados foram: {numbers[1]}')
