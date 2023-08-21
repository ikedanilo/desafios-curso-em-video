'''Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('==' * 15)
print('   Os 10 TERMOS DE UMA P.A   ')
print('==' * 15)

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
cont = 1
limite = 11
limite2 = 0

opcao = 'S'

while opcao == 'S':
    while cont < limite:
        a = a1 + (cont - 1) * r
        cont += 1
        print('{} > '.format(a), end='')
    opcao = str(input('Pausa\nDeseja mostrar mais termos [S/N]? ')).upper()
    if opcao == 'S':
        limite2 = int(input('Deseja mostrar mais quantos termos: '))
        limite = limite + limite2
print('*** fim ***')
