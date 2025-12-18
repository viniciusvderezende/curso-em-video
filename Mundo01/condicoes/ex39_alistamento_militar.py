from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade_atual = ano_atual - nascimento
idade_alistamento = 18

if idade_atual == idade_alistamento:
    print(f'Você já tem {idade_atual} anos e em {ano_atual} pode se alistar.')
elif idade_atual > idade_alistamento:
    print(f'Você deveria ter se alistado há {idade_atual - idade_alistamento} anos.')
    print(f'Seu alistamento foi em {ano_atual - idade_alistamento}.')
else:
    print(f'Ainda faltam {idade_alistamento - idade_atual} anos para o seu alistamento.')
    print(f'Você poderá se alistar em {ano_atual + (idade_alistamento - idade_atual)}.')