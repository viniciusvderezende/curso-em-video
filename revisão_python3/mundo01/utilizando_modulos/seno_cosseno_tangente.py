from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Para o ângulo de {angulo}°, temos:')
print(f'Seno: {seno:.2f}.')
print(f'Cosseno: {cosseno:.2f}.')
print(f'Tangente: {tangente:.2f}.')