frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {frase.count('A')} vezes nessa frase.')
print(f'Ela aparece pela primeira vez na posição de número {frase.find('A')+1}.')
print(f'A última letra a apareceu na posição de número {frase.rfind('A')+1}.')