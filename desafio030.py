# Crie um programa que leia um número inteiro qualquer e mostre se ele é par ou ímpar.

n = int(input('Digite um número inteiro: '))

if n % 2 == 0:
    print('{} é par!'.format(n))
else:
    print('{} é ímpar!'.format(n))
print('*** FIM ***')
