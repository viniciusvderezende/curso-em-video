numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1
        print('\33[33m', end='')
    else:
        print('\33[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {total} vezes.')
if total == 2:
    print('E por isso ele é um número primo.')
else:
    print('E por isso ele não é um número primo.')