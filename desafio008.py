#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
#Exercício Python 008 - Conversor de Medidas

m = float(input("Digite um valor em metros: "))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print("{}km".format(km))
print("{}hm".format(hm))
print("{}dam".format(dam))
print("{}m".format(m))
print("{}dm".format(dm))
print("{}cm".format(cm))
print("{}mm".format(mm))

print("\nA medida {}m corresponde a {}cm e {}mm".format(m, cm, mm))