from time import sleep

def maior(* numeros):
    contador = maior = 0
    print('-=-' * 30)
    print('Analisando os valores passados...')
    sleep(2)
    for valor in numeros:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nForam informados {contador} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    sleep(2)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()