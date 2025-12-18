from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
#radianos = radians(angulo)
print(f'O seno de {angulo}° é {sin(radians(angulo)):.2f}.')
print(f'O cosseno de {angulo}° é {cos(radians(angulo)):.2f}.')
print(f'A tangente de {angulo}° é {tan(radians(angulo)):.2f}.')