from random import randint
from time import sleep

print('-=-' * 15)
print(f'{'APOSTAS NA MEGA SENA':^45}')
print('-=-' * 15)
sleep(1)
lista = []
jogos = []
quantidade_jogos = int(input('Quantos jogos deseja que eu sorteie? '))
total_jogos = 1
while total_jogos <= quantidade_jogos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1

print('-=' * 6, f' SORTEANDO {quantidade_jogos} JOGOS ', '-=' * 6)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)