maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1: # Esse if diz: Se for o primeiro valor lido (primeiro laço), maior e menor receberão o valor digitado.
        maior = c
        menor = c
    else: # Agora é possível analisar os pesos comprarando com o peso do primeiro laço.
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print(f'O maior peso é o de {maior:.2f} Kg e o menor, {menor:.2f} Kg.')