def ficha(player, goals):
    if player == '':
        player = '<desconhecido>'
    if goals == '' or goals.isalpha():
        goals = '0'
    return f'O jogador {player} fez {goals} gol(s) no campeonato.'

jogador = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Número de gols: ')).strip()
print(ficha(jogador, gols))
