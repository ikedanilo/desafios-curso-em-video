'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
dados = dict()
temp = list()
lista = list()
while True:
    dados['jogador'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
    for cont in range(0, partidas):
        temp.append(int(input(f'Quantos gols na partida {cont}? ')))
    dados['gols'] = temp[:]
    dados['total'] = sum(dados['gols']) #'sum' soma todos os elementos da lista ou dicionário
    temp.clear()
    lista.append(dados.copy())
    print('=-'*30)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-'*20)
#print(lista)
print('cod ', end='')
for i in dados.keys(): #listando as chaves (keys) para montar o cabeçalho
    print(f'{i:<14} ', end='')
print()
print('-'*42)
for k, v in enumerate(lista):   #Listar a Lista
    print(f'{k:>3} ', end='')   #Printa a 'chave' da lista
    for d in v.values():    #Lista os valores do dicionário de acordo com o valor da lista
        print(f'{str(d):<15}', end='')
    print()
print('-'*42)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    elif opcao >= len(lista):
        print(f'Opção inválida. Não existe jogador com código {opcao}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {lista[opcao]["jogador"]}: ---')
        for i, g in enumerate(lista[opcao]['gols']):
            print(f'No jogo {i} fez {g} gols.')
print('< Volte Sempre >')
