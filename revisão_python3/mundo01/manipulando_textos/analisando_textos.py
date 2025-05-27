nome = input('Digite o nome completo: ').strip()

transformar_em_letras_maiusculas = nome.upper()
transformar_em_letras_minusculas = nome.lower()
dividir_nome = nome.split()
nome_sem_espacos = ''.join(dividir_nome)
primeiro_nome = dividir_nome[0]

print(f'Nome com todas as letras maiúsculas: {transformar_em_letras_maiusculas}')
print(f'Nome com todas as letras minúsculas: {transformar_em_letras_minusculas}')
print(f'Esse nome contém ao todo {len(nome)} letras.')
print(f'Esse nome contém {len(nome_sem_espacos)} sem contar os espaços.')
print(f'O primeiro nome contém {len(primeiro_nome)} caracteres.')

