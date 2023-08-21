''' Desafio 104: Crie um programa que tenha a função leiaint() que vai funcionar
de forma semelhante à função input() do python, só que
fazendo a validação para aceitar apenas um valor numérico.
ex:
n = leiaint('Digite um n')
'''
def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('ERRO! Digite um número inteiro válido.')
    return valor


#Programa Principal
n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
