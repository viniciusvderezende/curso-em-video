frase = input('Digite uma frase qualquer: ')

quantidade_vezes_aparece_a = frase.count('A')

print(f'A letra "A" aparece {quantidade_vezes_aparece_a} vez(es) na frase.')

print(f'Ela aparece pela última vez na posição {quantidade_vezes_aparece_a[-1::]}')