def notas(*n, sit=False):
    """
    --> Função para analisar notras e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação. 
    :return: Dicionário com as informações e situação da turma.
    """
    r = dict()
    r['total'] = len(n) # Conta a quantidade de elementos no dicinário
    r['maior'] = max(n) # Identifica o maior valor
    r['menor'] = min(n) # Identifica o menor valor
    r['media'] = sum(n) / len(n) # Soma os itens do dicionário e divide pela quantidade de elementos dentro dele.
    if sit: # Se o parâmetro sit=True, seja na declaração da função ou na variável resp, o sistema vai mostrar a situação do aluno.
        if r['media'] >= 7: # Se a chave média for...
            r['situacao'] = 'BOA' # Adiciona a chave situação e seu valor em razão da média das notas.
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal

resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)