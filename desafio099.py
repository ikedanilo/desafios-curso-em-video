'''Faça um programa que tenha uma função chamada MAIOR(), que recebe vários parâmetros
com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(* num):
    print('=-'*30)
    print('Analisando os valores passados...')
    cont = maior = 0
    for v in num:
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        print(v, end=' ')
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(1, 3, 45, 10, 3)
maior(123, 1, 2, 111)
maior(4, 3)
maior(9)
maior()
