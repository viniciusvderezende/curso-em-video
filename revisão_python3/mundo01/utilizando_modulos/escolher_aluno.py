from random import choice

primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')

lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
print(f'O aluno escolhido foi {choice(lista)}.')