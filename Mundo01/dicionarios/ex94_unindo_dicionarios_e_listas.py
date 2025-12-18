dados = dict()
pessoas = list()
soma = media = 0
contador = 1
while True:
    dados.clear()
    dados['nome'] = str(input(f'Digite o nome da {contador}ª pessoa: '))
    while True:
        dados['sexo'] = str(input(f'Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')            
    dados['idade'] = int(input(f'Idade de {dados['nome']}: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    
    while True:
        continuar = str((input('Quer continuar [S/N]? '))).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responsa somente S para SIM e N para NÃO!')
    if continuar == 'N':
        break
    contador += 1    
print('-=-' * 30)
print(f'A) Temos {len(pessoas)} pessoas cadastradas no total.')
media = soma / len(pessoas)
print(f'B) A média da idade das pessoas cadastradas é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for n in pessoas:
    if n['sexo'] in 'Ff':
        print(f'{n["nome"]} ', end='')
print()
print('D) Lista das pessoas que tem a idade acima da média: ', end='')
for n in pessoas:
    if n['idade'] >= media:
        print('   ', end='')
        for k, v in n.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<< ENCERRADO >>>>')