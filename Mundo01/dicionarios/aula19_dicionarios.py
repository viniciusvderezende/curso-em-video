# Adicionamos elementos às listas usando o comando append().

dados = list()
dados.append('Pedro')
dados.append(25)
for indice, dado in enumerate(dados):
    print(f'Índice: {indice} | Dado: {dado}')

# Todo elemento em um dicionário é chamado de "CHAVE", ou "KEYS".
# Nos dicionários, append() não funciona. Para isso, utilizamos a adição direta de itens.
dados = {'nome':'Pedro', 'idade':25} # Dicinário preexistente
dados['Sexo'] = 'M' # Adição do dado 'Sexo'.
print(dados['nome'])
print(dados['idade'])
print(dados['Sexo'])

# Para remover elementos de um dicionário, utilizamos del.
del dados['idade']
print(dados)

# Adicionar itens ao dicionário
filme = dict()
filme['Título'] = 'Star Wars'
filme['Ano'] = 1977
filme['Diretor'] = 'George Lucas'
print(filme) # imprime o dicinoário completo
print(filme.values()) # imprime os valores do dicinoário, que são atribuídos às chamves
print(filme.keys()) # imprime somente as chaves, ou os 'títulos' identificadores dos itens
print(filme.items()) # Imprime o dicinoário completo, com chaves e valores.

for k, v in filme.items():
    print(f'O {k} é {v}.')

pessoas = {'nome': 'Vinícius', 'Sexo': 'M', 'Idade': 36}
print(f'O {pessoas['nome']} tem {pessoas['Idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')


# Adicionar dicinários às listas
brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['Sigla'])
print(brasil[1]['UF'])

estado = {}
brasil = []
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Nas listas usamos [:] para gerar sua cópia, nos dicionários, somente copy() existe para esse fim.
print(brasil)

for e in brasil:
    print(e)

for e in brasil:
    print(e, end=', ')
print()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
