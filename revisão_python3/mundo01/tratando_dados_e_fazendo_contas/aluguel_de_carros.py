quilometros_percorridos = float(input('Quantos quilometros foram percorridos: '))
quantidade_dias = float(input('Por quantos dias o veículo foi alugado? '))

custo_quilometros_percorridos = quilometros_percorridos * 0.15
custo_quantidade_dias = quantidade_dias * 60
valor_total = custo_quantidade_dias + custo_quilometros_percorridos

print(f'O veículo foi alugado por {quantidade_dias} dias e percorreu {quilometros_percorridos:.2f} Km.')
print(f'Portanto, o custo do total da locação ficou em R$ {valor_total:.2f}')




#200 km = 30
#5 doas = 300