lista_jogadores = []
jogador = {}
lista_gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        lista_gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)
    lista_jogadores.append(jogador.copy())
    lista_gols.clear()
    jogador.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida. Tente novamente.')
    if continuar == "N":
        break
print('-=-' * 16)
print(f'{"cod":<4}{"nome":<20}{"gols":<20}{"total":<5}')
print('-' * 49)
for i, j in enumerate(lista_jogadores):
    print(f'{i:<4}', end='')
    for v in j.values():
        print(f'{str(v):20}', end='')
    print()
print('-' * 49)
option = 0
while option != 999:
    option = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if option >= len(lista_jogadores) and option != 999:
        print(f'ERRO! Não existe jogador com código {option}!')
    elif option < len(lista_jogadores):
        print(f' -- LEVANTAMENTO DO JOGADOR {lista_jogadores[option]["nome"]}:')
        for i, gol in enumerate(lista_jogadores[option]["gols"]):
            print(f'    No jogo {i + 1} fez {gol} gols.')
    print('-' * 49)
print('<< VOLTE SEMPRE >>')
