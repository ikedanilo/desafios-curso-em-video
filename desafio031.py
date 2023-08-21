# Faça um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas

d = float(input('Digite a distância da viagem em Km: '))

if d <= 200:
    c = d * 0.5
    print('Preço da passagem: R${:.2f}'.format(c))
else:
    c = d * 0.45
    print('Preço da passagem: R${:.2f}'.format(c))
print('Boa viagem!')
