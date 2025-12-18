'''lanches = ['Hamburguer', 'Milk Shake', 'Pizza', 'Pudim']
print(lanches)
print(len(lanches)) # Len Mostra a quantidade de itens da lista

lanches.append('Coockies') # Append insere um item ao final da lista.
print(lanches)
print(len(lanches))

lanches.insert(0,'Hot Dog') # insert insere um item e podemos escolher sua posição
print(lanches)
print(len(lanches))

lanches.insert(3,'Pavê') # insert insere um item e podemos escolher sua posição
print(lanches)
print(len(lanches))

del lanches[3] # del remove um item da lista e podemos selecionar o item pela posição
print(lanches)
print(len(lanches))

lanches.pop() # pop remove o último item da lista
print(lanches)
print(len(lanches))

lanches.pop(3) # pop normalmente é utilizado para remover o último parâmetro, más podemos fornecer seu índice para exlusão também
print(lanches)
print(len(lanches))

lanches.remove('Hot Dog') # remove retira o item pelo seu nome
print(lanches)
print(len(lanches))

if 'Hamburguer' in lanches:
    lanches.remove('Hamburguer')
    print(lanches)
    print(len(lanches))

if 'Chocolate' in lanches:
    lanches.remove('Chocolate')
    print(lanches)
    print(len(lanches))
else:
    print('Não encontrei Chocolate.')'''

valores = list(range(4, 11)) # list cria uma lista e, range, assim como no for, estabelece um alcance.
print(valores)

valores = list(range(4, 11, 2)) # list cria uma lista e, range, assim como no for, estabelece um alcance. O número dois, é o parâmetro que estabelece o intervalo do range.
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
print(valores)
print(len(valores))

valores.sort()
print(valores)
print(len(valores))

valores.sort(reverse=True)
print(valores)
print(len(valores))

num = [2, 5, 9, 1]
print(num)
num[2] = 3 # substitui o item da posição 2 (9) pelo valor (3)
print(num)

valores = []
valores.append(5)
valores.append(8)
valores.append(7)
valores.append(4)

for v in valores:
    print(f'{v}...', end=' ')

for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')

valor = list()
for cont in range(1, 5):
    valor.append(int(input(f'Digite o {cont}º valor: ')))
print(valor)

a = [2, 3, 4, 7]
b = a # Dessa forma, o sistema criauma ligação entre as listas e o que for alterado na losta B, será também na A.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] # Dessa forma, a variável B recebeu uma cópia de A, portanto, o que for alterado em B não será reproduzido em A.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')