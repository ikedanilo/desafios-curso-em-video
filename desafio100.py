'''Faça um programa que tenha uma LISTA chamada NUMEROS e duas funções chamadas SORTEIA() e
SOMAPAR(). A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(n, end=' ')
    print('PRONTO!')

def somapar(lst):
    soma = 0
    for cont in lst:
        if cont % 2 == 0:
            soma += cont
    print(f'Somando os valores pares de {lst}, temos {soma}.')


#PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somapar(numeros)
