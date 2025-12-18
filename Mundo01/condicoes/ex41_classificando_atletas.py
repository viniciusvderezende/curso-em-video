from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade_atual = ano_atual - nascimento

if idade_atual <= 9:
    print(f'Você tem {idade_atual} anos e se enquadra na categoria MIRIM!')
elif idade_atual <= 14:
    print(f'Você tem {idade_atual} anos e se enquadra na categoria INFANTL!')
elif idade_atual <= 19:
    print(f'Você tem {idade_atual} anos e se enquadra na categoria JÚNIOR!')
elif idade_atual <= 25:
    print(f'Você tem {idade_atual} anos e se enquadra na categoria SÊNIOR!')
else:
    print(f'Você tem {idade_atual} anos e se enquadra na categoria MASTER!')