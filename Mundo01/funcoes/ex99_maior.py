lista = []

def maior():
    maior = max(lista)
    print(f'O maior rnúmero da lista é {maior}.')
          

while True:    
    numeros = int(input('Digite um número: '))
    lista.append(numeros)        
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar not in 'S/N':
        print('Digite apenas S para sim ou N, para não!')
    if continuar == 'N':
        break
maior()