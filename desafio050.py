'''Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o'''

soma = 0
contpar = 0
for cont in range(1, 7):
    n = int(input('Digite o {}º número: '.format(cont)))
    if n % 2 == 0:
        soma += n
        contpar += 1
print('A soma dos {} números pares é igual a {}'.format(contpar, soma))
