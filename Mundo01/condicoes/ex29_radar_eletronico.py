velocidade = float(input('Digite a velocidade do veículo: '))
if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7
    print(f'''MULTADO! A velocidade da via é de, no máximo, 80 Km/h.
Você passou no radar a {velocidade} Km/h.
Sua multa custará R$ {multa:.2f}.''')
else:
    print(f'Você está na velocidade permitida pela via.')
print('Tenha um bom dia e dirija com segurança!')