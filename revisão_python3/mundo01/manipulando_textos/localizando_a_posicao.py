frase = input('Digite uma frase qualquer: ').strip().upper()

quantidade_vezes_aparece_a = frase.count('A')
aparece_primeira_vez = frase.find('A') + 1
aparece_ultima_vez = frase.rfind('A') + 1

print(f'A letra "A" aparece {quantidade_vezes_aparece_a} vez(es) na frase.')
print(f'A primeira letra "A" apareceu na posição {aparece_primeira_vez}.')
print(f'Ela aparece pela última vez na posição {aparece_ultima_vez}.')