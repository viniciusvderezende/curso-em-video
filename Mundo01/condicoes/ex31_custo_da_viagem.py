distancia = float(input('Qual é a distância até o destino? '))
ate_200_km = distancia * 0.50
maior_200_km = distancia * 0.45
if distancia <= 200:
    print(f'O custo da sua passagem será de R$ {ate_200_km:.2f}.')
else:
    print(f'O custo da sua passagem será de R$ {maior_200_km:.2f}')
print(f'Tenha uma boa viagem!')