
def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto OPCIONAL!'
    else:
        return f'Com {idade} anos: Voto OBRIGATÓRIO!'


ano_nascimento = int(input('Digite o ano de nascimento da pessoa: '))
print(voto(ano_nascimento))

