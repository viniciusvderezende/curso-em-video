nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi {media}. REPROVADO.')
elif media >= 7.0:
    print(f'Sua média foi {media}. APROVADO.')
else:
    print(f'Sua média foi {media}. RECUPERAÇÃO.')