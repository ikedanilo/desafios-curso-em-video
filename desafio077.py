'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
           'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

print(palavras)

for cont in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[cont]} temos ', end='')
    if palavras[cont].count('A') != 0:
        print('a', end=' ')
    if palavras[cont].count('E') != 0:
        print('e', end=' ')
    if palavras[cont].count('I') != 0:
        print('i', end=' ')
    if palavras[cont].count('O') != 0:
        print('o', end=' ')
    if palavras[cont].count('U') != 0:
        print('u', end=' ')
print(f'\n{" --- FIM --- ":^30}')
