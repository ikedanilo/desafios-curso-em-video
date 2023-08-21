''' Crie um programa que joque jokenpô com você'''
from random import choice
from time import sleep

print('{:=^40}'.format(' JOOOOOOOKEEEEENNN....PÔ! '))

print('''Opções...
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('Escolha sua jogada: '))

# Condicoes de jogadas do Jogador
if opcao == 1:
    jogada = 'pedra'
elif opcao == 2:
    jogada = 'papel'
elif opcao == 3:
    jogada = 'tesoura'
else:
    jogada = ''
    print('Jogada inválida.')

lista = ['pedra', 'papel', 'tesoura']  # Lista de jogadas do Computador
computador = choice(lista)             # Escolha aleatória do Computador

# Condicoes: Jogador x Computador
if jogada != '':
    print('JOO...')
    sleep(1)
    print('KEEEN...')
    sleep(1)
    print('PÔ!')
    print('-=' * 30)
    if computador == jogada:
        print('Empate! Os dois escolheram {}'.format(jogada))
    elif computador == 'pedra' and jogada == 'papel' or computador == 'papel' and jogada == 'tesoura' \
            or computador == 'tesoura' and jogada == 'pedra':                                         # "\" quebra linha
        print('Você ganhou! Você escolheu {} e o computador {}'.format(jogada, computador))
    else:
        print('Você perdeu! Você escolheu {} e o computador {}'.format(jogada, computador))
else:
    print('Jogue novamente com alguma jogada válida.')
