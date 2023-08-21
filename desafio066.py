'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é
a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS digitados
e qual foi SOMA entre eles (desconsiderando a flag 999).'''

cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números digitados foi {soma}')
