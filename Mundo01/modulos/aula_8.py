'''import math # Importada toda a biblioteca de matemática.

numero = int(input('Digite um número: '))
raiz = math.sqrt(numero)
print(f'A raiz quarada de {numero} é {math.ceil(raiz)}.') #math.ceil arredonda para cima os números decimais.
print(f'A raiz quarada de {numero} é {math.floor(raiz)}.') #math.floor arredonda para baixo os números decimais.

from math import sqrt, ceil, floor

numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print(f'A raiz quarada de {numero}, arredondada para cima, é: {ceil(raiz)}.') # ceil arredonda para cima os números decimais.
print(f'A raiz quarada de {numero}, arrdondada para baixo, é: {floor(raiz)}.') # floor arredonda para baixo os números decimais.

import random

num = random.randint(1, 10)
print(num)'''

import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is fun :red_heart:', variant='emoji_type'))
print(emoji.emojize('Python is fun :polegar_para_cima:', language='pt'))

print(emoji.emojize(':rosto_chorando_de_rir:', language='pt'))
print(emoji.emojize('😂'))
