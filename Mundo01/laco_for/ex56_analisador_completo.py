soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menores_20_anos = 0

for c in range(1, 5):
    print(f'----- {c}a PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('idade: '))
    sexo = input('Sexo: [M/F]').strip().upper()
    soma_idade += idade

    if c == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
        
    if sexo == "F" and idade < 20:
        mulheres_menores_20_anos += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chana {nome_homem_mais_velho}.')
print(f'No total, {mulheres_menores_20_anos} mulheres tem menos de 20 anos.')