'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

cont18 = contho = cont20m = 0

while True:
    print('---' * 10)
    print('CADASTRE UMA PESSOA')
    print('---' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contho += 1
    if sexo == 'F' and idade < 20:
        cont20m += 1
    print('---' * 10)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Número de pessoas maiores de 18 anos: {cont18}')
print(f'Quantidade de homens cadastrados: {contho}')
print(f'Quantidade de mulheres menores de 20 anos: {cont20m}')
