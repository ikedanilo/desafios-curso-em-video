''' Desafio 102: Crie um programa que tenha uma função FATORIAL() que
receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado SHOW, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo do fatorial.
'''

def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
        if show == True:
            if cont != 1:
                print(f'{cont} x ', end='')
            else:
                print(f'{cont} = ', end='')
    return fat


#Programa Principal
num = int(input('Digite um número: '))
help(fatorial)
print(fatorial(num, show=True))
