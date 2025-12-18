contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove', 'dez', 
            'onze', 'doze', 'treze', 'catorze', 'quinze', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número inteiro entre 0 e 20 para ver seu nome por extenso: '))
        if 0 <= numero <= 20:
            break
        print('Opção inválida. ', end='')
    print(f'O número digitado foi o {contagem[numero]}.')

    while True:
        continuar = str(input(f'Deseja continuar [S/N]? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Opção inválida. ', end='')

    if continuar == 'N':
        break
print('Fim do programa.')