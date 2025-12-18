from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ').upper()
aluno2 = input('Digite o nome do segundo aluno: ').upper()
aluno3 = input('Digite o nome do terceiro aluno: ').upper()
aluno4 = input('Digite o nome do quarto aluno: ').upper()
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = choice(lista)
print(f'O aluno escolhido foi: {sorteio}.')