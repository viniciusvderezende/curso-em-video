times = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 
    'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
    'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
    'Red Bull Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá'
)

cinco_primeiros = times[0:5]
quatro_ultimos = times[-4:]
ordenados = sorted(times)
posicao = times.index('Corinthians')

print('-=-' * 40)
print(f'Os 5 primeiros colocados no campeonato são: {cinco_primeiros}.')
print('-=-' * 40)
print(f'Os quatro últimos colocados são: {quatro_ultimos}.')
print('-=-' * 40)
print(f'Seus nomes em ordem alfabética são: {ordenados}.')
print('-=-' * 40)
print(f'O Corinthians está na {posicao + 1}ª posição do campeonato.')
print('-=-' * 40)
