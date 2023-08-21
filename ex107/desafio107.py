#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
p = float(input('Digite um preço : R$'))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}.')
print(f'O aumento 10% de {p:.2f} é R${moeda.aumento(p, 10):.2f}.')
print(f'A diminuição 15% de {p:.2f} é R${moeda.diminuir(p, 15):.2f}.')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}.')
