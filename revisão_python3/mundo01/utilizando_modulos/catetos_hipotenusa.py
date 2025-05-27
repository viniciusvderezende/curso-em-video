from math import hypot, sqrt

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa tem o valor de {hipotenusa:.2f}.') #Usando o módulo hypot (hipotenusa).
print(f'A hipotenusa tem o valor de {sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2):.2f}.') #Usando o módulo sqrt (raiz quadrada).

#Forma matemática da solução

print(f'A hipotenusa tem o valor de {((cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5):.2f}.')