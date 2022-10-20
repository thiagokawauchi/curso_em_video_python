jogador = {}
lista_gols = []
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    lista_gols.append(int(input(f'Quantos gols na partida {c}? ')))
print('-=-' * 20)
jogador['gols'] = lista_gols[:]
jogador['total'] = sum(lista_gols)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {sum(jogador["gols"])} gols.')
