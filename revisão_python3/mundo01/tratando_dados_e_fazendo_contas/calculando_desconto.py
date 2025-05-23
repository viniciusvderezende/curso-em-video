preco = float(input('Digite o preço do produto: R$ '))
desconto = preco * 0.05
novo_preco = preco - desconto

print(f'O preço do produto com 5% de desconto passará a ser R$ {novo_preco:.2f}.')