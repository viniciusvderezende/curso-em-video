cont = 0
n = 0
soma = 0
n = int(input('Digite um valor entre 1 e 999: '))
while n != 999:
    cont += 1 
    soma += n
    n = int(input('Digite um valor entre 1 e 999: '))
print(f'Foram digitados {cont} números.')
print(f'A soma de todos os números digitados é {soma}.')