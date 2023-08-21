'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total
de gols feitos durante o campeonato.'''
'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
dados = dict()
temp = list()
time = list()
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    npartidas = int(input(f'Quantidade de partidas que {dados["nome"]} jogou: '))
    for cont in range(0, npartidas):
        temp.append(int(input(f'Gols feitos no jogo {cont}: ')))
    dados['gols'] = temp[:]
    dados['total'] = sum(dados['gols'])
    temp.clear()
    time.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print(time)
print('cod ', end='')
for e in dados.keys():  #Formando Cabeçalho
    print(f'{e:<15}', end='')
print()
print('--'*30)
for k, v in enumerate(time):    #Trazendo valores da lista e dicionário
    print(f'{k:>3} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end='')  #precisou colocar STR por causa da lista que está no dicionário 'gols'
    print()
print('--'*30)
while True:
    resp = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if resp == 999:
        break
    elif resp >= len(time):
        print(f'ERRO! Não existe jogador para o número {resp}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR: {time[resp]["nome"].upper()} --')
        for k, v in enumerate(time[resp]['gols']):
            print(f'\tNo jogo {k} fez {v} gols.')
print('<<<< FIM >>>>')