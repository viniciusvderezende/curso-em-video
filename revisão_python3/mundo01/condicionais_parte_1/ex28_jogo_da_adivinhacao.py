# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "pensar" em um número.
print('-=-' * 20)
print('Vou pensar em um número. Tente adivinhar qual é.')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar.
print('Processando...')
sleep(2)
if computador == jogador:
    print(f'Parabéns! Eu pensei no número {computador} e você acertou!')
else:
    print(f'Que pena! Eu pensei no número {computador} e você não acertou!')
sleep(1)
print('Fim.')