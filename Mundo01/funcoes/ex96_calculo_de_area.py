def calcular_area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.2f}m² x {comprimento:.2f}m² corresponde a {area:.2f}m².')


print('-' * 20)
print(f'{'Cálculo de Área':^20}')
print('-' * 20)
print
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
calcular_area(largura, comprimento)