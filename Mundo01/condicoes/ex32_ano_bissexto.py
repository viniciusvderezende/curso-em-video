from datetime import date

ano = int(input('Digite o ano para saber se ele é bissexto (coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é um ano bissexto.')
else:
    print(f'O ano de {ano} não é um ano bissexto.')