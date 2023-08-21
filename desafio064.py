'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag 999)'''

n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        cont += 1
        soma = soma + n

print('Quantidade de números digitados: {}'.format(cont))
print('Soma dos números digitados: {}'.format(soma))
