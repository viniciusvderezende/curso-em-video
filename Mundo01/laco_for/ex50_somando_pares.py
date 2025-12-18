soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input(f'Digite o {c}° número: '))
    if numero % 2 == 0:
        pares = numero
        soma += pares
        cont += 1
        
if cont < 1:
    print(f'Você não digitou nenhum número par.')
elif cont == 1:
    print(f'Você digitou apenas um número par, que foi o {pares}.')
else:
    print(f'A soma dos {contador} números pares é {soma}.')