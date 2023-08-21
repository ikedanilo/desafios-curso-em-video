'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
lista = list()
dados = dict()
totidade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    totidade += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip()[0]
        if resp in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp in 'Nn':
        break
print('=-'*20)
#print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {totidade/len(lista):.2f} anos.')
print(f'c) A lista de mulheres cadastras é: ',end='')
for cont in lista:
    if cont['sexo'] in 'Ff':    #Se forem mulheres as pessoas cadastradas na lista
        print(f'[{cont["nome"]}] ', end='')
print()
print(f'D) Pessoas com idade maior que a média de {totidade/len(lista):.2f} anos: ')
for cont in lista:
    if cont['idade'] > (totidade/len(lista)): #Se idade for maior que a média de idade de pessoas cadastradas
        for k, v in cont.items():
            print(f'\t{k} = {v}; ', end='')
        print()
