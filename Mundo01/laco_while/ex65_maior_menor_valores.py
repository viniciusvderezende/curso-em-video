continuar = 'S'
contador = 0
soma = 0
media = 0
menor = 0
maior = 0
while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    contador += 1
    soma += n
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
media = soma / contador
print(f'Foram digitados {contador} números e a média de todos eles é {media:.2f}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')