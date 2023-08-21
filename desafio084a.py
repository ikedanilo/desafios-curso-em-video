'''
Faça um programa que leia NOME e PESO de várias pessoas, guardando tudo em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas (maior peso e nome das pessoas)
c) Uma listagem com as pessoas mais leves (menor peso e nome das pessoas)
obs: usar 'Quer continuar?'
'''
pessoas = list() #lista auxiliar para copiar Estrutura para final
final = list()
cont = 0
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(final) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    final.append(pessoas[:]) #copia lista 'pessoas' para lista 'final'
    pessoas.clear() #exclui lista 'pessoas' para no proximo laço while ele criar uma nova estrutura
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('*-'*50)
print(final)
print(f'Foram cadastradas {len(final)} pessoas.')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='') #Analise do(s) nome(s) de MENOR PESO
for p in final:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print('')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='') #Analise do(s) nome(s) de MAIOR PESO
for p in final:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
