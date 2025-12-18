'''numeros = list()
for n in range(1, 6):
    numeros.append(int(input(f'Digite o {n}º número: ')))
print('-=-' * 25)
print(f'Os números digitados foram: {numeros}.')
print('-=-' * 25)
print(f'O maior valor digitado foi o {max(numeros)} e ele aparece na posição {numeros.index(max(numeros)) + 1} da lista.')
print('-=-' * 25)
print(f'O menor valor digitado foi o {min(numeros)} e ele aparece na posição {numeros.index(min(numeros)) + 1}.')
print('-=-' * 25)'''

valores = []
maior = 0
menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-=-' * 25)
print(f'Os números digitados foram: {valores}.')
print('-=-' * 25)
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
print('-=-' * 25)