'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
 tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
 No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from operator import itemgetter #Biblioteca usada para Organizar Dicionário
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = dict() #declaração de dicionário para Rankear dicionário JOGO
print('Valores sorteados:')
for i, j in jogo.items():   #Sorteio dos dados para cada jogador
    print(f'{i} tirou {j} no dado.')
print(jogo)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Itemgetter - Rankear Dicionário selecionando qual valor
print(ranking)
# Obs: Ranking passa a ser uma LISTA
print('-='*15)
print(' == RANKING DOS JOGADORES == ')
for x, y in enumerate(ranking):
    print(f'{x+1}º lugar: {y[0]} com {y[1]}.')
