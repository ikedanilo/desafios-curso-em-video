'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores (21 anos)'''

from datetime import date

anoatual = date.today().year
maior = 0
menor = 0

for cont in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(cont)))
    idade = anoatual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Maioridade: {} pessoas\nMenoridade: {} pessoas'.format(maior, menor))
