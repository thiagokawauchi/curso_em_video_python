print('-=-' * 20)
tabela_brasileirao = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo',
                      'Fluminense', 'Athletico-PR', 'Atlético-MG', 'América-MG',
                      'Botafogo', 'Fortaleza', 'Santos', 'São Paulo',
                      'Bragantino', 'Goiás', 'Coritiba', 'Seará SC',
                      'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Lista de times do Brasileirão: {tabela_brasileirao}')
print('-=-' * 20)
print(f'Os 5 primeiros são {tabela_brasileirao[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos são {tabela_brasileirao[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('-=-' * 20)
print(f'O Corinthians está na {tabela_brasileirao.index("Corinthians") + 1}ª posição')
