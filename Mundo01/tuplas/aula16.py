lanches = ('Amoras', 'Bananas', 'Caju', 'Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanches[::-1])
print(lanches[2][3])
print(len(lanches))

for comida in lanches:
    print(f'Eu vou comer: {comida}.')
print('Comi demais!')

for comida in lanches[::-1]:
    print(f'Eu vou comer: {comida}.')
print('Comi demais!')

for c in range(0, len(lanches)):
    print(f'{lanches}', end=' - ')
print('Comi demais!')


for c in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[c]}.')
print('Comi demais!')

for c in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[c]} na posição {c}.')
print('Comi demais!')

for posicao, comida in enumerate((lanches)):
    print(f'Eu vou comer {comida} na posição {posicao}.')
print('Comi demais!')

print(f'{sorted(lanches)}') # sorted organiza os itens em ordem crescente, más transofrma em uma lista.
print(f'{sorted(lanches)[::-1]}') # sorted organiza os itens em ordem crescente e [::-1, inverte a ordem], más transforma em uma lista.

a = (2, 4, 5)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) # Quantas vezes aparecem o número 5 na variável c?
print(c.index(8)) # Informa em qual posição está localizado o item 8.

pessoa = ('Vinícius', 36, 'Andréia', 37, 98.56)
print(pessoa)
del(pessoa) # del apaga a variável dos registros.
print(pessoa)