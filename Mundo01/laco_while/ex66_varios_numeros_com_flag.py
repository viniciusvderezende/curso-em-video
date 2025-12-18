soma = cont = 0

while True:
    n = int(input('Digite um número inteiro (digite 999 para parar): '))
    if n == 999:
        break
    else:
        soma += n
        cont += 1
print(f'Foram digitados {cont} números e sua soma é {soma}.')