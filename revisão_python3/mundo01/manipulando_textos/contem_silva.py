nome = input('Digite o nome completo: ')

contem_silva = 'Silva' in nome

if contem_silva == True:
    print('Essa pessoa tem Silva no seu nome.')
else:
    print('Essa pessoa não tem Silva no nome.')