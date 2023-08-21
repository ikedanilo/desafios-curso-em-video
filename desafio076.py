'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular.'''

listagem = ('Lápis', 1.75,
         'Caneta', 2.50,
         'Papel sulfite', 0.50,
         'Borracha', 2.30,
         'Lapiseira', 7.20,
         'Livro', 152.90)
print('-'*33)
print(f'{" LISTAGEM DE PREÇOS ":^31}')
print('-'*33)
for cont in range(0, len(listagem), 2):
    print(f'{listagem[cont]:.<20}.....R${listagem[cont+1]:>6}')
print('-'*33)
