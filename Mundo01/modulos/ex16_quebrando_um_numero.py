from math import trunc

numero = float(input('Digite um número: '))
print(f'O valor digitado foi {numero} e sua porção inteira é {trunc(numero)}.')
print(f'O valor digitado foi {numero} e sua porção inteira é {numero // 1:.0f}.')
print(f'O valor digitado foi {numero} e sua porção inteira é {int(numero)}.')
