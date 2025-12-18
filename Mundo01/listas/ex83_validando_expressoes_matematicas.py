expressao = str(input('Digite uma expressão: '))

lista = []
for s in expressao:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')