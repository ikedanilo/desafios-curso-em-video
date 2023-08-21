'''Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequencia de Fibonacci
ex: 0 > 1 > 1 > 2 > 3 > 5 > 8 '''

elem = int(input('Qtd de elementos da seq. Fibonacci: '))

cont = 0
a = 0
b = 1

while cont < elem:
    acum = a
    print(acum, end=' > ')
    c = a + b
    a = b
    b = c
    cont += 1
print('Acabou')
