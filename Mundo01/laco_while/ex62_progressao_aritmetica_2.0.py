from time import sleep

print('=-=' * 11)
print('----- PROGRESSÃO ARITMÉTICA -----')
print('=-=' * 11)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} - ', end='')
        termo += razao
        cont += 1
    print('PAUSA.')
    mais = int(input('Quando termos mais você deseja ver? '))
print('Finalizando...')
sleep(2)
print(f'Progressão finalizada com {total} termos mostrados.')