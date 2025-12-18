cidade = input('Digite o nome de uma cidade: ').strip().upper()
separar = cidade.split()
inicio = separar[0] in 'SANTO'
print(inicio)

cidade = input('Digite o nome de uma cidade: ').strip().upper()
inicio = cidade[:5]
print(inicio in 'SANTO')
print(inicio == 'SANTO')