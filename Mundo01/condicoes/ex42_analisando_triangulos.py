lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Esses segmentos podem formar um triângulo', end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO.')
    else:
        print('iSÓSCELES.')
else:
    print('Os segmentos acima não podem formar um triângulo.')