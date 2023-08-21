'''Mostre um programa que leia o peso de 5 pessoas e no final
mostre qual é o maior e o menor peso lidos'''

maior = 0
menor = 0

for n in range(1, 6):
    peso = float(input('Digite o peso (kg) da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        else:
            menor = peso

print('---' * 20)
print('Maior peso: {}kg'.format(maior))
print('Menor peso: {}kg'.format(menor))
