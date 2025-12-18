from math import hypot, sqrt

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa1 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5
hipotenusa2 = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
hipotenusa3 = hypot(cateto_oposto, cateto_adjacente)
print(f'O valor da hipotenusa é {hipotenusa1:.2f}.')
print(f'O valor da hipotenusa é {hipotenusa2:.2f}.')
print(f'O valor da hipotenusa é {hipotenusa3:.2f}.')