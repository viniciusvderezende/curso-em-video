recebe_nota_1 = float(input('Digite a primeira nota: '))
recebe_nota_2 = float(input('Digite a segunda nota: '))
recebe_nota_3 = float(input('Digite a terceira nota: '))
recebe_nota_4 = float(input('Digite a quarta nota: '))

soma_notas = recebe_nota_1 + recebe_nota_2 + recebe_nota_3 + recebe_nota_4
media_notas = soma_notas / 4

print(f'A média das notas é {media_notas:.2f}')