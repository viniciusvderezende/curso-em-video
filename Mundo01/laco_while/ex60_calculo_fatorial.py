from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O Fatorial de {n} é {f}.')



n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1 # Fator nulo no fatorial é 1.
print(f'Calculando {n}!: ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else  ' = ', end='') # Acrescenta o x para indicar a multiplicação entre os fatores, remome o último x e coloca o sinal de igualdade no final.
    f *= c # Fatorial x contador.
    c -= 1 # Carregando os fatores em ordem decrescente.
print(f'{f}.')
