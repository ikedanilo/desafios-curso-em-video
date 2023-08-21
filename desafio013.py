# Exercício Python #013​ - Reajuste Salarial
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input("Salário: R$"))

novo = salario * 1.15

print("Salário: R${:.2f}\nNovo Salário: R${:.2f}".format(salario, novo))
