#Exercício Python #012 - Calculando Descontos
# Faça um algortimo que leia um preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Digite o preço do produto: R$"))

final = preco - (preco * 0.05)

print("O preço R${:.2f} com 5% de desconto é igual a R${:.2f}".format(preco, final))
