# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input("Digite o valor do Cateto Adjacente: "))

h = hypot(co, ca)

print("O valor da Hiponetusa do triângulo retângulo é {:.2f}".format(h))
