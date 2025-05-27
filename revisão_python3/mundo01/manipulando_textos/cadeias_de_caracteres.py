#Fatiamento de strings

frase = 'Curso em Vídeo Python'

print(frase[9]) # Entre colchetes [] há o item que deve retornar, ou seja, na frase, a letra "v" representa a posição nº 9.
print(frase[9:14]) # A palavra "vídeo" vai da posição nº 9 até 13, sendo que a posição 14 não será exibida.
print(frase[9:21:2]) # A leitura ocorrerá da posição 9 até a 21, pulando de duas em duas letras.
print(frase[:5]) # A ausência de números antes dos dois pontos, representa que iniciará em 0 e vai até a posição 5.
print(frase[15:]) # a ausência de números após o dois pontos, indica que ele iniciará na posição 15 e irá até o final.
print(frase[9::3]) # A ausência de números entre "::" significa que não estamos informando onde termina o fatiamento, ou seja, vai até o final pulando de 3 em 3.
print(len(frase)) # Len vem de length (comprimento) da frase, ou seja, conta os espaços ocupados pelos caracteres e espaços entre eles.
print(frase.count('o')) # Count conta quantas vezes uma letra é exibida na frase.
print(frase.count('o', 0, 13)) # Count conta quantas vezes uma letra é exibida na frase e os números, mostram onde começa a contagem e até onde vai.
print(frase.find('deo')) # Find localiza determinado conjunto de caracteres e retorna sua posição na cadeia de caracteres. Caso não existam, retornará o valor -1.
print('Curso' in frase) # In retorna True ou False se a cadeia de caracteres existir ou não em determinado conjuntos de letras.

# Módulos de transformação de strings

print(frase.replace('Python', 'Android')) # Replace substitui os itens em uma lista (substituiu Python por Android).
print(frase.upper()) # Upper transforma todos os caracteres em maiúsculos.
print(frase.lower()) # Lower transforma todos os caracteres em minúsculos.
print(frase.capitalize()) # Captalize transforma a primeira letra da frase em maiúscula.
print(frase.title()) # Title analisa onde há espços e transforma as letras após um espaço em maiúsculas.
print(frase.strip()) # Strip remove os espaços antes e depois de uma cadeia de caracteres
print(frase.rstrip()) # Rstrip remove os espaços somente à direita da frase.
print(frase.lstrip()) # Lstrip remove os espaços somente à esquerda da frase.

# Módulos de divisão de strings

print(frase.split()) # Split localiza os espaços entre as palavras e cria uma lista onde cada palavra passa a ser um elemento independente. Ex: Curso em Vídeo Python passará a ser ['Curso', 'em', 'Vídeo', 'Python'].
dividido = frase.split()
print(dividido[2][3]) # Estamos pegando o segundo item da lista e mostrando o terceiro caractere dele, ou seja, a palavra 'Vídeo' e a letra 'e'.

# Módulos de junção de strings
frase = frase.split()
print('-'.join(frase)) # Join junta as palavras da lista que dividimos acima e, nesse caso, insere um traço entre as palavras.