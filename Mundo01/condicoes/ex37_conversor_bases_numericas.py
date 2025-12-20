numero = int(input('Digite um número inteiro para ver sua conversão: '))
base = int(input('''Escolha a opção para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Digite a sua opção: '''))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
if base == 1:
    print(f'O número {numero} convertido em base binária é: {binario[2:]}.')
elif base == 2:
    print(f'O número {numero} convertido em base octal é: {octal[2:]}.')
elif base == 3:
    print(f'O número {numero} convertido em base hexadecimal é: {hexadecimal[2:]}.')
else:
    print('Essa opção não existe.')