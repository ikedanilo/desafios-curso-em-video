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
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    final.append(pessoas[:]) #copia lista 'pessoas' para lista 'final'
    pessoas.clear() #exclui lista 'pessoas' para no proximo laço while ele criar uma nova estrutura
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('*-'*50)
print(final)
print(f'Foram cadastradas {len(final)} pessoas.')
maior = menor = 0
for i, v in enumerate(final): # Analise do PESO maior e menor
    if i == 0:
        menor = maior = v[1]
    elif v[1] > maior:
        maior = v[1]
    elif v[1] < menor:
        menor = v[1]
print(f'O menor peso foi de {menor}Kg. Peso de ', end='') #Analise do(s) nome(s) de MENOR PESO
for i, v in enumerate(final):
    if v[1] == menor:
        print(f'{v[0]} ', end='')
print('')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='') #Analise do(s) nome(s) de MAIOR PESO
for i, v in enumerate(final):
    if v[1] == maior:
        print(f'{v[0]} ', end='')
