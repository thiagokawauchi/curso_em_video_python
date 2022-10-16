numbers_list = []
for c in range(0, 5):
    number = int(input('Digite um valor: '))
    if c == 0 or number >= numbers_list[-1]:
        numbers_list.append(number)
        print('Valor inserido no final da lista...')
    else:
        for i, n in enumerate(numbers_list):
            if number <= n:
                numbers_list.insert(i, number)
                print(f'Valor inserido na posição {i} da lista...')
                break # Este break evita looping infinito por recursão
print('-=-' * 10)
print(numbers_list)
