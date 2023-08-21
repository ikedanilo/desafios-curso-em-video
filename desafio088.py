'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
 cadastrando tudo em uma lista composta.'''
from random import randint # Import de biblioteca randint

jogo = list()   #Definição das listas
jogofim = list()

print('****** SORTEIO MEGA-SENA ******')
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'=-=-=-=-= SORTEANDO {qtd} JOGOS =-=-=-=-=')

for cont in range(0, qtd): #For para qtd de jogos
    for x in range(0, 6):   #For para criar os 6 números de cada jogo
        n = randint(1, 60)
        if cont == 0:
            jogo.append(n)
        else:
            while n in jogo:    #Caso o número for repetido, fazer novo sorteio de um novo número
                n = randint(1, 60)
            jogo.append(n)
    cont += 1
    jogofim.append(jogo[:]) #Copiar lista para uma outra final, criando uma estrutura
    jogo.clear()

for y, v in enumerate(jogofim):   #Escrever todos os jogos finais com os números em ordem crescente
    jogofim[y].sort()
    print(f'Jogo {y+1}: {v}')
print(f'=-=-=-=-= BOA SORTE! =-=-=-=-=')
