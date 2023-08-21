# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

max = n1
min = n1

if n2 > max:
    max = n2
if n3 > max:
    max = n3

if n2 < min:
    min = n2
if n3 < min:
    min = n3

print('{} é o maior número'.format(max))
print('{} é o menor número'.format(min))
