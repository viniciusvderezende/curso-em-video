salario_atual = float(input('Digite o valor do salário atual: R$ '))
if salario_atual > 1250.00:
    salario_aumento = salario_atual + salario_atual * 0.10
else:
    salario_aumento = salario_atual + salario_atual * 0.15
print(f'Seu salário passará a ser R$ {salario_aumento:.2f} após o reajuste.')
