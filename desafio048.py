'''Faça um programa que faça a soma de todos os números ímpares
que são múltiplos de 3 e que encontram no intervalo de 1 até 500'''

soma = 0
cont = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma += n
        cont += 1
print('A soma dos {} números ímpares divisíveis por 3 que se encontram no'
      ' intervalo de 1 até 500 é igual a {}.'.format(cont, soma))
