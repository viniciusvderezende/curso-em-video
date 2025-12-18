from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    opcao = int(input('>>>>>Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} resulta em {soma}.')
        print('=-=' * 10)
    
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print(f'O resultado de {valor1} x {valor2} é igual a {multiplicar}.')
        print('=-=' * 10)
    
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'entre {valor1} e {valor2} o maior valor é o {maior}.')
        print('=-=' * 10)
    
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    
    elif opcao == 5:
        print('Finalizando...')
        print('=-=' * 10)
        sleep(2)
    
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre!')