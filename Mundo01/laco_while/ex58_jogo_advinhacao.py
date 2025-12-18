from random import randint

cont = 1
print('-=-' * 10)
print(F'{'JOGO DA ADIVINHAÇÃO':^30}')
print('-=-' * 10)
print('')
print('Eu pensei em um número entre 0 e 10 e quero que tente adivinhar.')
computador = randint(0, 10)
jogador = int(input('Qual é o seu palpite? '))
while jogador != computador:
    if computador > jogador:
        jogador = int(input(f'Maior que {jogador}. Tente novamente: '))
        cont += 1
    else:
        jogador = int(input(f'Menor que {jogador}. Tente novamente: '))
        cont += 1
print(f'Parabéns, cocê acertou! Eu pensei no número {computador}!')
print(f'Foram necessárias {cont} tentativas para você adivinhar')

print('-=-' * 10)
print(F'{'JOGO DA ADIVINHAÇÃO':^30}')
print('-=-' * 10)
print('')
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Tente adivinhar.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'Maior do que {jogador}. Tente novamente.')
        elif jogador > computador:
            print(f'Menor que {jogador}. Tente novamente.')
print(f'Acertou! Foram necessárias {palpites} tentativas.')