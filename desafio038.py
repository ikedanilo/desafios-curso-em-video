'''Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:
- O Primeiro valor é maior
- O Segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor é maior. {} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo valor é maior. {} é maior que {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais.')
