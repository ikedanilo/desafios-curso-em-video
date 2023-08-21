'''Faça um programa que tenha uma função chamada CONTADOR() que receba trê parâmetros:
início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada.
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Um contagem personalizada'''
from time import sleep

def contador(i, f, p):
    """

    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    if i <= f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for cont in range(i, f+1, p):
            print(cont, end=' ')
            sleep(0.25)
    elif i > f:
        if p == 0:
            p = 1
        if p < 0:
            p = -p
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for cont in range(i, f-1, -p):
            print(cont, end=' ')
            sleep(0.25)
    print('FIM!')
    print('=-'*30)


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
help(contador)