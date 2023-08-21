#Faça um programa que leia um ângulo qualquer e mostre
# na tela do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan

ang = float(input("Digite um ângulo em graus: "))

rad = radians(ang)

print("Sen({}º) = {:.2f}".format(ang, sin(rad)))
print("Cos({}º) = {:.2f}".format(ang, cos(rad)))
print("Tan({}º) = {:.2f}".format(ang, tan(rad)))