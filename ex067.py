while True:
    number = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if number < 0:
        break
    for c in range(1, 11):
        print(f'{number} x {c:2} = {number * c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
