from time import sleep
time = list()
partidas = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    total_partidas = int(input(f'Nº de partidas jogadas por {jogador["nome"]}: '))
    partidas.clear()
    for c in range(1, total_partidas + 1):
        partidas.append(int(input(f'   Quandos gols foram marcados na {c + 1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f' {k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar os dados de qual jogador? (999 para encerrar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i + 1} fez {g} gols.')
            sleep(1)
    print('-' * 40)
print('<< VOLTE SEMPRE >>')