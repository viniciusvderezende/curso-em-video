sexo = input('Digite o sexo da pessoa: [M/F]: ').strip().upper()[0] # [0] representa a leitura da primeira letra, caso seja digitada a palara completa em vez da inicial.
while sexo != 'M' and sexo != 'F':
    print('Opção inválida!')
    sexo = input('Digite o sexo da pessoa: [M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')