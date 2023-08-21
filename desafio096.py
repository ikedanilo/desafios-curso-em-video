'''Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''
def area(a, b):
    print(f'A área de um terreno {a} x {b} é de {a*b:.2f}m².')


# Programa Principal
print('Controle de terrenos')
print('-'*20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
