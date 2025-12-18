matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_colunas = 0

# Gerando a matriz
for l in range(0, 3): # Gerando as linhas [l]
    for c in range(0, 3): # Gerando as colunas [c]
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')) # input dos valores (matriz[l][c]).

print('-=-' * 30)

for l in range(0, 3): # Gerando a linha da matriz
    for c in range(0, 3): # Gerando a coluna da matriz
        print(f'[{matriz[l][c]:^5}]', end='') # Imprimindo a matriz com o espaçcamento uniforme de cada item (matriz[l][c]:^5)
        if matriz[l][c] % 2 == 0: # Condicional da paridade
            soma_pares += matriz[l][c] # Soma dos pares da matriz
    print()
print('-=-' * 30)
print(f'A soma dos valores pares é {soma_pares}.')

for l in range(0, 3): # iteração das linhas
    soma_colunas += matriz[l][2] # somando os valores da última coluna [2] em função de cada linha [l]
print(f'A soma dos valores da coluna 3 é: {soma_colunas}.')

for c in range(0, 3):
    if c == 0: # Se o primeiro item é vazio
        maior = matriz[1][c] # O maior elemento é p primeiro digitado
    elif matriz[1][c] > maior: # se a linha 1 coluna c for maior que o maior
        maior = matriz[1][c] # O maior recebe a linha 1 coluna c
print(f'O maior valor da segunda linha é o {maior}.')