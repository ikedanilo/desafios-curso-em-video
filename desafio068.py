'''Faça um programa que jogue PAR ou ÍMPAR com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
cont = 0
while True:
    valor = int(input('Diga um valor: '))
    jogada = ' '
    pc = randint(0, 10)
    final = valor + pc
    while jogada not in 'PpIi':   #confere se variável JOGADA tem algum falor de P ou I
        jogada = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print('--'*20)
    print(f'Você jogou {valor} e o computador {pc}. Total de {final} ', end='')
    print('DEU PAR' if final % 2 == 0 else 'DEU ÍMPAR')
    if jogada == 'P':
        if final % 2 == 0:
            print('--' * 20)
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            break
    if jogada == 'I':
        if final % 2 == 0:
            break
        else:
            print('--' * 20)
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
    print('=-'*20)
print('=-'*20)
print('Você PERDEU!')
print(f'GAME OVER! Você venceu {cont} vezes')
