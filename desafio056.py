'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo
- qual é o nome do homem mais velho
- quantas mulheres tem menos de 20 anos'''

somaidade = 0
velho = 0
menor20 = 0
nomevelho = ''

for cont in range(1, 5):
    print('---- {}ª pessoa ----'.format(cont))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    somaidade = somaidade + idade

    if idade > velho and sexo == 'M':
        nomevelho = nome
        velho = idade

    if sexo == 'F' and idade < 20:
        menor20 = menor20 + 1
        nomemulhernova = nome

print('*** RESULTADOS ***')
print('Média de idade: {:.2f}'.format(somaidade / 4))
print('Homem mais velho: {} de {} anos'.format(nomevelho, velho))
print('Qtd de mulher abaixo dos 20 anos: {}'.format(menor20))
