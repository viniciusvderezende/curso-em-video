preco = float(input('Digite o preço do produto: R$ '))
forma_pagamento = int(input('''\nQual será a forma de pagamento:
                            
[1] - À vista no dinheiro / Cheque
[2] - À vista no cartão de crédito
[3] - 2x no cartão de crédito
[4] - 3x ou mais no cartao de crédito
                            
Digite a sua opção: '''))

if forma_pagamento == 1:
    a_vista_dinheiro_cheque = preco - (preco * 10 / 100)
    print(f'O preço com desconto de 10% é R$ {a_vista_dinheiro_cheque:.2f}.')

elif forma_pagamento == 2:
    a_vista_cartao = preco - (preco * 0.05)
    print(f'O preço com desconto de 5% é R$ {a_vista_cartao:.2f}.')

elif forma_pagamento == 3:
    valor_parcelas = preco / 2
    print(f'O preço para parcelamento em 2x no cartão é R$ {preco:.2f}.')
    print(f'Esse valor foi parcelado em 2x de R$ {valor_parcelas:.2f}.')

elif forma_pagamento == 4:
    parcelas = int(input('Você deseja parcelar esse valor em quantas vezes? '))
    valor_com_juros = preco + (preco * 0.20)
    valor_parcelas = valor_com_juros / parcelas
    print(f'O preco para parcelamento em 3x ou mais é R$ {valor_com_juros:.2f} com 20% de juros.')
    print(f'Esse valor foi parcelado em {parcelas}x de R$ {valor_parcelas:.2f}.')

else:
    print('Você digitou uma opção inválida. Selecione outra opção.')
