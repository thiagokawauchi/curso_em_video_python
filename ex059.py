from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0

while option != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    option = int(input('>>>>> Qual é a sua opção? '))
    if option == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}.')
    elif option == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}.')
    elif option == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}.')
        else:
            print(f'Os valores {n1} e {n2} são iguais.')
    elif option == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')