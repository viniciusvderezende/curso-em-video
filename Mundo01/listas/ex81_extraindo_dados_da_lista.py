numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    print('Adicionado com sucesso.')
    continuar = str(input(f'Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

numeros.sort(reverse=True)
print(f'foram digitados {len(numeros)} números.')
print(f'Esses são os valores ordenados de forma decrescente: {numeros}.')
if 5 in numeros:
    print('o número 5 faz parte da lista.')
else:
    print('O número 5 não foi encontrado na lista.')