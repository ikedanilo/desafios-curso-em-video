#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from ex108 import moeda
p = float(input('Digite um preço : R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O aumento 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumento(p, 10))}.')
print(f'A diminuição 15% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p, 15))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
