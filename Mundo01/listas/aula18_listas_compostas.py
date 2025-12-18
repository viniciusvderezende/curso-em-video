pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0]) # Mostra o indice 0 do item zero da lista maior.
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])    # Mostra o item 1 completo, com seus dois itens na lista maior.

teste = []
teste.append('Vinícius')
teste.append(36)
time = list()
time.append(teste[:]) # [:] representa a cópia da lista. Isso é necessário para evitar que todas as alterações realizadas na lista sejam replicadas. Quando fazemos a cópia, preservamos a lista original e modificamos somente a cópia.
teste[0] = 'Maria'
teste[1] = 22
time.append(teste[:])

print(teste)
print(time)


equipe = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(equipe[0][1])
for p in equipe:
    # print(p) # Para mostrar somente um índice de cada item, basta adicinar o [0], [1] etc.
    print(f'{p[0]} tem {p[1]} anos de idade.')

equipe = list()
dado = list()
total_maior = total_menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('idade: ')))
    equipe.append(dado[:]) # estamos pegando uma cópia de dado ([:]) e inserindo na lista equipe.
    dado.clear() # excluindo a lista dado.
print(equipe)

for p in equipe:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')