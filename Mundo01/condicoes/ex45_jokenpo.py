from random import randint
from time import sleep

print('-=-' * 10)
print(f'{'JOKENPÔ':^30}')
print('-=-' * 10)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('''\nQual é a sua jogada?
                    
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
                    
Sua opção: '''))

if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVÁLIDA! ESCOLHA UMA OPÇÃO ENTRE 0, 1 E 2!')
else:
    print('-=-' * 11)
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('-=-' * 11)
    print(f'Computador jogou {itens[computador]}.')
    print('')
    print(f'Jogador jogou {itens[jogador]}.')
    print('')

    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        elif jogador == 2:
            print('COMPUTADOR VENCEU!')

    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('VOCÊ VENCEU!')

    elif computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('EMPATE!')