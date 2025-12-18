print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)
print('')

termo = int(input('Digite o primero termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = termo + (10 - 1) * razao
for c in range(termo, decimo_termo + razao, razao):
    print(f'{c}', end=' - ')
print('Fim.')