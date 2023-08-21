'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.'''
valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor da Posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    elif valores[cont] > maior:
        maior = valores[cont]
    elif valores[cont] < menor:
        menor = valores[cont]
print('*-' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O menor valor é {menor} na Posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print(f'\nO maior valor é {maior} na Posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
