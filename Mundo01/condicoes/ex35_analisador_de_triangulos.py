print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

segmento1 = float(input('Digite o valor do primeiro seguimento: '))
segmento2 = float(input('Digite o valor do segundo seguimento: '))
segmento3 = float(input('Digite o valor do terceiro seguimento: '))
if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Essas medidas formam um triângulo!')
else:
    print('Essas medidas não podem formar um triângulo!')