''' Desafio 103: Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais:
o NOME de um jogador e quantos GOLS ele marcou.
O programa deverá ser capaz de mostrar a FICHA DO JOGADOR mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


#Programa principal
nome = str(input('Nome do Jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
