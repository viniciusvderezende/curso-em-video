recebe_medida = float(input('Digite uma medida em metros: '))

converter_centimetros = recebe_medida * 100
converter_milimetros = recebe_medida * 1000
representacao_centimetros = recebe_medida / 100
representacao_milimetros = recebe_medida / 1000

print(f'{recebe_medida:.2f} metro(s) corresponde(m) a {converter_centimetros:.2f} centimetro(s), ou {representacao_centimetros} metro(s).')
print(f'{recebe_medida:.2f} metro(s) corresponde(m) a {converter_milimetros:.2f} milimetro(s), ou {representacao_milimetros} metro(s).')