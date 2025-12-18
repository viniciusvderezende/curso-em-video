from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Eu vou pensar em um número de 0 à 5. Tente adivinhar...')
print('-=-' * 20)
usuario = int(input('Em qual número eu pensei? '))
print('Processando...')
sleep(2)
if usuario == computador:
    print(f'Parabéns! Eu pensei justamente no número {computador}! Você venceu!')
else:
    print(f'Que pena, você errou... Eu pensei no número {computador} e não no {usuario}.')