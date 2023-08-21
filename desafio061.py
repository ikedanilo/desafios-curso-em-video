'''Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão - USANDO WHILE'''

print('==' * 15)
print('   Os 10 TERMOS DE UMA P.A   ')
print('==' * 15)

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 1

while cont < 11:
    a = a1 + (cont - 1) * r
    cont += 1
    print(a, end=' > ')
print('FIM')
