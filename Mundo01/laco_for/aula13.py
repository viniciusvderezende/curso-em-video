for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(0, 11, 2):
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)

inicio = int(input('Digite o início do laço: '))
fim = int(input('Digite o final do laço: '))
passo = int(input('Digite o passo para o laço: '))
for c in range(inicio, fim, passo):
    print(c)
print('fim')

s = 0
for c in range(1, 5 + 1):
    n = int(input(f'Digite o {c}° número: '))
    s += n
print(f'A soma dos {c} números foi {s}.')