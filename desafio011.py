#Exercício Python #011​ - Pintando Parede
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input("Digite a largura: "))
a = float(input("Digite a altura : "))

area = l * a

tinta = area / 2

print("Para uma parede com área de {}m² deve-se usar {} litros de tinta".format(area, tinta))
