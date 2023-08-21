''' Crie um programa que joque jokenpô com você'''
from random import choice

print('JOOOOKEEEEENNNN....PÔ!')
escolha = str(input('Escolha (pedra, papel ou tesoura): '))

lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)

if computador == escolha:
    print('Empate! Os dois escolheram {}'.format(escolha))
elif computador == 'pedra' and escolha == 'papel' or computador == 'papel' and escolha == 'tesoura':
    print('Você ganhou! Você escolheu {} e o computador {}'.format(escolha, computador))
else:
    print('Você perdeu! Você escolheu {} e o computador {}'.format(escolha, computador))
