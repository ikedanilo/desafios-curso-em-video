'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''

def notas(*n, sit=False): #o asterisco permite que seja lido vários valores
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas de alunas (aceita várias)
    :param sit: valor opcional se deve ou não adicionar situação da turma
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 6:
            r['sit'] = 'Aprovado'
        else:
            r['sit'] = 'Reprovado'
    return r


#Programa Principal
resp = notas(4, 4.1, 9.3, 7.9, 6.6, sit=True)
help(notas)
print(resp)
