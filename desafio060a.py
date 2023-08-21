''' Faça um programa que leia um número qualquer e mostre o seu fatorial
USANDO FOR'''

o = n = int(input('Digite um número: '))
fat = n

for n in range(n, 1, -1):
    fat = fat * (n - 1)
print('O fatorial de {}! é igual a {}'.format(o, fat))
