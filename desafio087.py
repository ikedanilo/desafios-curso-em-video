'''Exercício Python 087: Aprimore o desafio anterior (matriz 3x3), mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):   #Ler matriz
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor [{i}][{j}]: '))
print('=-'*30)
for i in range(0, 3):   #Escrever matriz
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
print('=-'*30)
somatot = somacol3 = 0
for i in range(0, 3): # Soma de todos os valores
    for j in range(0, 3):
       somatot += matriz[i][j]
print(f'Soma de todos os valores da matriz: {somatot}')

for i in range(0, 3):   # Soma dos valores da coluna 2 (terceira coluna)
    somacol3 += matriz[i][2]
print(f'Soma de valores da coluna 3 matriz: {somacol3}')

maior = matriz[1][0]    #Maior valor da Segunda Linha da matriz
for j in range(0, 3):
    if matriz[1][j] > maior:
        maior = matriz[1][j]
print(f'O maior valor da segunda linha é {maior}')
