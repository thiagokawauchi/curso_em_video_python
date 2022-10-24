def notas(*nota, status=False):
    '''
    -> Funcão para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas do aluno (aceita várias).
    :param status: valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    '''
    dicio = {}
    dicio['total'] = len(nota)
    dicio['maior'] = max(nota)
    dicio['menor'] = min(nota)
    total_notas = 0
    for n in nota:
        total_notas += n
    dicio['media'] = total_notas / len(nota)
    if status:
        if dicio['media'] < 5:
            dicio['situacao'] = 'RUIM'
        elif dicio['media'] < 7:
            dicio['situacao'] = 'RAZOÁVEL'
        elif dicio['media'] < 9:
            dicio['situacao'] = 'BOA'
        else:
            dicio['situacao'] = 'EXCELENTE'
    return dicio


# Programa principal
resposta = notas(5.5, 9.5, 10, 6.5, status=True)
print(resposta)
help(notas)
