#Exercício Python #014- Conversor de Temperaturas
# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

c = float(input("Temperatura em ºC: "))
f = ((9*c)/5)+32

print("A temperatura {:.1f}ºC corresponde a {:.1f}ºF".format(c, f))
