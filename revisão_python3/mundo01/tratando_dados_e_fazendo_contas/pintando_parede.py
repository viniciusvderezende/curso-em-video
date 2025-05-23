# Calcular quantos litros de tinta são necessários para pontar uma parede. Cada litro de tinta pinta 2 metros quadrados.

largura_parede = float(input('Digite a largura da parede: '))
altura_parede = float(input('Digite a altura da parede: '))
calcular_area_parede = largura_parede * altura_parede
quantidade_tinta = calcular_area_parede / 2

print(f'A parede tem a dimensão de {largura_parede:.2f} x {altura_parede:.2f} e área total de {calcular_area_parede:.2f}m².')
print(f'Portanto, serão necessários {quantidade_tinta:.2f} litros de tinta para cobrir toda a área dessa parede.')