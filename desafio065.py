'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar.'''

cont = 0
resp = 'S'
soma = 0
maior = menor = 0

while resp == 'S':
    qtd = int(input('Quantidade de números a digitar: '))
    while cont < qtd:
        n = int(input('Digite um número inteiro: '))
        soma = soma + n
        if cont == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        cont += 1
        if cont == qtd:
            resp = str(input('Deseja continuar [S/N]: ')).upper()
            if resp == 'S':
                qtd2 = int(input('Quantidade de números a digitar: '))
                qtd = qtd + qtd2
print('*** RESPOSTA ***')
print('Média dos números somados = {:.2f}'.format(soma / cont))
print('Maior número: {}\nMenor número: {}'.format(maior, menor))
