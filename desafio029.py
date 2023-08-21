# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80 km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$ 7,00 por cada km acima do limite.

v = int(input('Digite a velocidade do carro em km/h: '))

if v > 80:
    multa = (v - 80) * 7
    print('Você foi multado! O valor da multa será de R${:.2f}'.format(multa))
else:
    print('Você não foi multado. Continue assim!')
print('*** FIM ***')
