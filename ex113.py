def leia_int():
    while True:
        try:
            num_inteiro = int(input('Digite um Inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num_inteiro


def leia_float():
    while True:
        try:
            num_real = float(input('Digite um Real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num_real


n1 = leia_int()
n2 = leia_float()
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
