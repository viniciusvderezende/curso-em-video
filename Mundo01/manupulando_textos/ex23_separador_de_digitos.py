numero = int(input('Digite um número entre 1 e 9999: '))
num = str(numero)
print(f'Analisando o número {numero}...')
print(f'Unidade: {num[3]}.')
print(f'Dezena: {num[2]}.')
print(f'Centena: {num[1]}.')
print(f'Milhar: {num[0]}.')

numero = int(input('Digite um número entre 1 e 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {unidade}.')
print(f'Dezena {dezena}.')
print(f'Centena: {centena}.')
print(f'Milhar {milhar}.')