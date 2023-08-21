#Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a
#mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no
#desafio 108.

from ex109 import moeda
p = float(input('Digite um preço : R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O aumento 10% de {moeda.moeda(p)} é {moeda.aumento(p, 10, True)}.')
print(f'A diminuição 15% de {moeda.moeda(p)} é {moeda.diminuir(p, 15, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
