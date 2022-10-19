from time import sleep
lista = []
pessoa = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Nota 1: ')))
    pessoa.append(float(input('Nota 2: ')))
    lista.append(pessoa[:])
    pessoa.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if continuar not in 'SN':
            print('Opção inválida. Digite novamente.')
        else:
            break
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'{"No.":4}{"NOME":20}{"MÉDIA":>6}')
print('-' * 30)
for c, valor in enumerate(lista):
    print(f'{c:<4}', end='')
    print(f'{lista[c][0]:<20}', end='')
    print(f'{(lista[c][1] + lista[c][2]) / 2:>6.1f}')
print('-' * 60)
option = 0
while option != 999:
    option = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if option != 999:
        print(f'Notas de {lista[option][0]} são ', end='')
        print(f'[{lista[option][1]}, {lista[option][2]}]')
        print('-' * 60)
print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
