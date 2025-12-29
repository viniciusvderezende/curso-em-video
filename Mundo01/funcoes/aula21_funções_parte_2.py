# # help()
# # help(print)
# # print(input.__doc__)

# # Docstrings
# '''from time import sleep

# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ', flush=True)
#         c+=p
#         sleep(0.5)
#     print('Fim!')


# contador(2, 10, 2)
# help(contador)

# # Parâmetros opcionais

# def somar(a, b, c=5):
#     s = a + b + c
#     print(f'A soma vale {s}.')

# somar(3, 2, 5)
# somar(8, 4)


# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite mais um número: '))
# n3 = int(input('Digite o último número: '))

# def soma (a=0, b=0, c=0):
#     s = a + b + c
#     print(f'O resultado será {s}.')

# soma()


# def soma (a=n1, b=n2, c=n3):
#     s = a + b + c
#     print(f'O resultado será {s}.')

# soma()


# def soma (a=0, b=0, c=0):
#     s = n1 + n2 + n3
#     print(f'O resultado será {s}.')

# soma()


# def somando (a=0, b=0, c=0):
#     s = a + b + c
#     print(f'O resultado será {s}.')

# somando(b=4, c=2)

# def sum(a=0, b=0, c=0):
#     somatoria = a + b + c
#     print(f'O resultado será {somatoria}.')

# sum(n1, n2, n3)'''

# # Escopo de variáveis

#     # Escopo Local: As variáveis estão dentro das funções e limitadas a elas.

# def teste():
#     x = 8
#     print(f'No programa printcipal, n vale {n}.')
#     print(f'No programa printcipal, x vale {x}.')


#  # Escopo Global: As variáves estão fora das funções e acessíveis a todo o sistema.
# n = 2
# print(f'No programa printcipal, n vale {n}.')
# teste()
# # print(f'No programa printcipal, x vale {x}.')

# a = 5 # Escopo Global

# def teste(b):
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}.') # Escopo Local
#     print(f'B dentro vale {b}.') # Escopo Local
#     print(f'C dentro vale {c}.') # Escopo Local

# teste(a)

# print(f'A fora vale {a}.') # Escopo Global

# def teste(b):
#     global a # Aplica ao valor da variável Loca à variável Global, portanto, a deixa de ser 5 e passa a ser 8.
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}.') # Escopo Local
#     print(f'B dentro vale {b}.') # Escopo Local
#     print(f'C dentro vale {c}.') # Escopo Local

# teste(a)

# print(f'A fora vale {a}.') # Escopo Global

# # Retorno de valores

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'O resultado é {s}.')

# somar(1, 2, 3)
# somar(1, 2)
# somar(1)

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s

# resp = somar(1, 2, 3)
# print(somar(1, 2, 3))
# print(f'com a função return: {resp}.')

# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram: {r1}, {r2} e {r3}.')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são: {f1}, {f2} e {f3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

if par(num):
    print('É par.')
else:
    print('Não é par.')