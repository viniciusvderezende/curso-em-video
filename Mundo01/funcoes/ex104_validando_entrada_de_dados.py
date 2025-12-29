def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE APENAS VALORES INTEIROS!\033[m')
        if ok:
            break
    return valor


n = leia_int('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')