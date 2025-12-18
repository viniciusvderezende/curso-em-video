from random import randint
from time import sleep
print('=-=' * 10)
print(f'{'Jogo do PAR ou ÍMPAR':^30}')
print('=-=' * 10)

cont = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('PAR ou ÍMPAR [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e eu, {computador}. Total de {total}.')
    if opcao == 'P':
        if total % 2 == 0:
            print(f'{total} é PAR. Você venceu!')
            cont += 1
        else:
            print(f'{total} é IMPAR. Você perdeu!')
            break
    elif opcao == 'I':
        if total % 2 != 0:
            print(f'{total} é ÍMPAR. Você venceu!')
            cont += 1
        else:
            print(f'{total} é PAR. Você perdeu!')
            break
    print('Vamos jogar novamente...')
    sleep(2)        
print(f'Você venceu {cont} partidas consecutivas.')