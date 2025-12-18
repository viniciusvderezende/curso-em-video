custo_compra = 0
produtos_maiores_mil = 0
nome_mais_barato = ''
mais_barato = 0
contador = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    contador += 1

    custo_compra += preco
    if preco > 1000.0:
        produtos_maiores_mil += 1
    if contador == 1 or preco < mais_barato: # essa linha simplifica o uso do else comentado.
        mais_barato = preco
        nome_mais_barato = produto
    '''else:
        if preco < mais_barato:
            mais_barato = preco
            nome_mais_barato = produto'''

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R$ {custo_compra:.2f}.')
print(f'Foram adquiridos {produtos_maiores_mil} maiores que R$ 1.000,00.')
print(f'O produto mais barato é o {nome_mais_barato} e custou R$ {mais_barato:.2f}.')