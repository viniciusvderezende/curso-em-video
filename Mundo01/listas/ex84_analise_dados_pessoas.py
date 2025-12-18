pessoas = []
dados = []
pesadas = leves = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0: # Se não houver nada na lista:
        pesadas = leves = dados[1] # peso (que é dados[1] é igual ao maior e ao menor peso, que é 0)
    else:
        if dados[1] > pesadas:
            pesadas = dados[1]
        if dados[1] < leves:
            leves = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
        
print('-=-' * 30)
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.' )
print(f'O maior peso foi de {pesadas}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesadas:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leves}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leves:
        print(f'[{p[0]}] ', end='')