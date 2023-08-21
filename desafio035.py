# Faça um programa que leia o comprimento de três retas e diga se
# ao usuário se elas podem ou não formar um triângulo

from math import fabs

a = float(input('Digite o tamanho do lado a: '))
b = float(input('Digite o tamanho do lado b: '))
c = float(input('Digite o tamanho do lado c: '))

if fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b:
    print('É possível formar Triângulo!')
else:
    print('Não forma triângulo...')
