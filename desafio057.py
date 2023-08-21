'''Faça um programa que pergunte o sexo e só aceite M ou F '''

sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado inválido. Digite o sexo [M/F]: ')).upper().strip()[0]

if sexo == 'M':
    print('Sexo Masculino')
elif sexo == 'F':
    print('Sexo Feminino')
