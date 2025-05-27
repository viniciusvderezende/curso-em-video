from random import shuffle

primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista) #Shuffle não funciona quando inserido diretamente na print, pois ele modifica a lista diretamente na lista (in-place) e não retorna uma nova lista. Para que funcione, devemos chamar o mõdulo antes de imprimir na tela.
print(f'A ordem de apresentação dos trabalhos é: {lista}.')
