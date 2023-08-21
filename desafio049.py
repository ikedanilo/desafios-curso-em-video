'''Refaça o desafio 009, mostrando a tabuada de um número que o
usuário escolher só que agora usando o laço for'''

n = int(input('Digite um número: '))

for cont in range(1, 11):
    print('{} x {} = {}'.format(n, cont, n * cont))
print('fim')
