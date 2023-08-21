'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    while resp != "S" and resp != "N":
        resp = str(input('Valor inválido... Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('*-'*30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem DECRESCENTE são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')
