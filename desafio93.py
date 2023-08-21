'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.'''
dados = dict()
temp = list()
dados['jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
for cont in range(0, partidas):
    temp.append(int(input(f'Quantos gols na partida {cont}? ')))
dados['gols'] = temp[:]
dados['total'] = sum(dados['gols']) #'sum' soma todos os elementos da lista ou dicionário
print(dados)
print('=-'*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for x, y in enumerate(dados['gols']): #Como dados['gols'] é uma lista então usamos o enumerate
    print(f'\t=> Na partida {x}, fez {y} gols.')
