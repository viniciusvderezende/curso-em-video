material_escolar = (
    'Caderno Capa Dura', 25.50,
    'Caneta Azul', 3.75,
    'Lápis Preto', 1.50,
    'Borracha', 2.00,
    'Régua 30cm', 5.90,
    'Mochila Reforçada', 120.99,
    'Estojo Simples', 15.00,
    'Caixa de Lápis de Cor', 35.80,
    'Marca-texto Amarelo', 6.50
)

print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
for posicao in range(0, len(material_escolar)):
    if posicao % 2 == 0:
        print(f'{material_escolar[posicao]:.<30}', end='')
    else:
        print(f'R${material_escolar[posicao]:>7.2f}')
print('-' * 40)