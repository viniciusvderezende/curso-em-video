valor_casa = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é o valor do seu salário: R$ '))
prazo_quitacao = float(input('Em quantos anos pretente pagar o empreéstimo? '))
prestacao = valor_casa / prazo_quitacao
percentual_salario = salario * 0.30
print(f'Para pagar uma casa no valor de R$ {valor_casa:.2f} em {prazo_quitacao} anos, o valor das parcelas será de {prestacao:.2f}.')
if prestacao <= percentual_salario:
    print(f'O valor da prestação é R$ {prestacao:.2f}, o que fica abaixo dos 30% do seu salário, que corresponde a {percentual_salario:.2f}. Seu empreéstimo foi aprovado.')
else:
    print(f'O valor de R$ {prestacao:.2f} excede os 30% do seu salário, que correspondem a {percentual_salario:.2f}. Seu empreéstimo foi negado.')

    