'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
 e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
listanum = list()
while True:
    n = int(input('Digite um valor: '))
    if n in listanum:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        listanum.append(n)
        print('Valor adicionado!')
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        resp = str(input('Digite uma resposta válida. Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('*-'*30)
print(f'Sua lista é {listanum}')
listanum.sort()         # Ordenando em Ordem Crescente
print(f'Lista em ordem Crescente é {listanum}')
