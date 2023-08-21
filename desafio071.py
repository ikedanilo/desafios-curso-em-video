'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('{:-^41}'.format(' BANCO SIRI CASCUDO '))

#nota50 = nota20 = nota10 = nota1 = 0

saque = int(input('Digite o valor de saque: R$'))

nota50 = saque // 50
resto = saque % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota1 = resto // 1

print(f'Nota de 50 {nota50}')
print(f'Nota de 20 {nota20}')
print(f'Nota de 10 {nota10}')
print(f'Nota de 1 {nota1}')
