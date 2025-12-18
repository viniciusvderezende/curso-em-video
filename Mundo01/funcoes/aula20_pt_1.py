# Funções são utilizadas para realizar tarefas rotineiras e que podem ser reaproveitadas.

def mostraLinha():
    print('-' * 10)


mostraLinha()
print('      CURSO EM VÍDEO     ')
mostraLinha()
mostraLinha()
print('      APRENDENDO PYTHON     ')
mostraLinha()
mostraLinha()
print('      VINÍCIUS REZENDE     ')
mostraLinha()

def mensagem(msg):
    print('-' * 10)
    print(msg)
    print('-' * 10)
mensagem('      SISTEMA DE ALUNOS')

def titulo(txt):
    print('-' * 10)
    print(txt)
    print('-' * 10)


titulo('       O MELHOR CURSO     ')
titulo('      APRENDENDO PYTHON     ')
titulo('       VINÍCIUS REZENDE     ')

def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(2, 6)
soma(7, 8)
soma(a = 4, b = 5)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B é igual a {s}.')


soma(b = 4, a = 5)

def contador(*num):
    print(num)
    

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')    

contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

def contador(*num):
    tam = len(num)    
    print(f'Recebi os valores {num} e ao todo são {tam}.')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)