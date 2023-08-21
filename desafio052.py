'''Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo'''

n = int(input('Digite um número: '))

soma = 0

for cont in range(1, n+1):
    resto = n % cont
    if resto == 0:
        soma += 1

if soma == 2:
    print('{} é PRIMO'.format(n))
else:
    print('{} NÃO é PRIMO'.format(n))
