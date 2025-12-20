def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'{mensagem:^{tamanho}}')
    print('~' * tamanho)


escreva('Olá')
escreva('Vinícius Vasconcelos de Rezende')
escreva('Python Lover')