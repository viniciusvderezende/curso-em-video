from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano_atual - nascimento >= 18:
        maior += 1
    else:
        menor += 1
print(f'No total, {maior} pessoas atingiram a maioridade e {menor} pessoas ainda são menores de idade.')
