'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = qtd1000 = menor = 0
barato = ''

print('{:-^40}'.format(' LOJÃO DO DANILO '))

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    total += preco
    if preco > 1000:
        qtd1000 += 1
    if total == preco:
        menor = preco
        barato = produto
    if preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
    print('---'*10)
print('{:-^40}'.format(' EXTRATO '))
print(f'Total gasto: R${total:.2f}')
print(f'Qtd produtos acima de R$1000,00: {qtd1000}')
print(f'Produto mais barato: {barato} / Preço R${menor:.2f}')
