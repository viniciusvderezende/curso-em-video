frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))#coloca as letras em maiúsculas e conta o que está em aprenteses.
print(len(frase)) #conta o tamanho da frase.
print(len(frase.strip())) #strip remove os espaços da frase e len conta os caracteres.
print(frase.replace('Python', 'Java')) #replace substitui o termo descrito somente nesse print. Para trocar o termo da variável, deve-se atribuir isso na variável, como por exemplo: farase = frase.replace('Python', 'Java').
print('Curso' in frase) # Mostra se o termo existe na string.
print(frase.find('Vídeo')) # Mostra em qual posição o termo se inicia na string.
print(frase.split()) # Separa todos os termos da string por vírgula onde existirem os espaços entre os termos e armazena em uma lista.
dividido = frase.split()
print(dividido[0]) # Mostra o item da lista após a divisão, sendo o número dentro de colchetes a posição do item.
print(dividido[2][3]) # Mostra o caractere do item da lista após a divisão, sendo o primeiro número a posição do termo na lista e, o segundo número dentro de colchetes, a posição do caractere dentro do termo.