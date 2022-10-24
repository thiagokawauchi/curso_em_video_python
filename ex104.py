def leiaInt(solicitacao):
    print('-' * 30)
    while True:
        number = str(input(solicitacao))
        if number.isnumeric():
            int(number)
            break
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return number


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
