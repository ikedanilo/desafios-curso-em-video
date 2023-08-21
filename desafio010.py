#Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre qunatos dólares ela pode comprar
#Considere US$1,00 = R$3,27

reais = float(input("Digite o valor em reais que você tem na carteira: R$"))
dolar = reais / 3.27

print("Com R${:.2f} você pode comprar US${:.2f}".format(reais, dolar))
