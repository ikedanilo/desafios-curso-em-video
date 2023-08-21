'''Desenvolva um programa que leia o primeiro termo e
a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão'''
print('==' * 15)
print('   Os 10 TERMOS DE UMA P.A   ')
print('==' * 15)

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

for cont in range(1, 11):
    a = a1 + (cont - 1) * r
    print(a, end=' > ')
print('*** fim ***')
