# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#exemplo: Digite um número: 6.127. O número 6.127 tem a parte inteira 6
import math

n = float(input("Digite um número: "))

print("A parte inteira de {} é {}".format(n, math.trunc(n)))