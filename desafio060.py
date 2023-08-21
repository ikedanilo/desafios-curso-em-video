''' Faça um programa que leia um número qualquer e mostre o seu fatorial'''

n = int(input('Digite um número: '))
cont = n
fat = 1

print('Calculando {}!'.format(n), end=' = ')
while cont > 0:
    print('{} '.format(cont), end='')
    print('x ' if cont > 1 else '= ', end='')
    fat = fat * cont
    cont = cont - 1
print('{}'.format(fat))
