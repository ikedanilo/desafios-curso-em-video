#Exercício Python #015- Aluguel de Carros
#Escreva um programa que pergunte a quantidade Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado

km = float(input("Km percorridos: "))
d = int(input("Quantidade de dias do carro alugado: "))
preco = d * 60 + km * 0.15

print("O preço final do carro alugado durante {} dias e {}km percorridos é de R${:.2f}".format(d, km, preco))