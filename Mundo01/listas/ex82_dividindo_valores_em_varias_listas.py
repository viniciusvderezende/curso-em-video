valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os valores digiados foram: {valores}.')
print(f'Valores pares: {pares}.')
print(f'Valores ímpares: {impares}.')