maiores_18 = 0
homens = 0
mulheres_20 = 0

while True:
    print('-' * 30)
    print(f'{'CADASTRE OUTRA PESSOA':^30}')
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_20 += 1
        
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
   
print(f'{maiores_18} tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres_20} mulheres tem menos que 20 anos.')