partidas = list()
jogador = dict()
jogador['nome'] = str(input('Digite o nome do Jogador: '))
total_partidas = int(input(f'Nº de partidas jogadas por {jogador["nome"]}: '))
for c in range(1, total_partidas + 1):
    partidas.append(int(input(f'   Quandos gols foram marcados na {c}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-' * 30)
print(jogador)
print('-=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas no campeonato.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i + 1}, fez {v} gols.')
print(f'Total de gols: {jogador['total']}.')
print('-=-' * 30)