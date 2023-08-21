'''Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais outro valor: ')),
     int(input('Digite o último valor: ')))
print('-=' * 20)
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vez(es)')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Valores pares digitos foi: ', end='')
for cont in range(0, 4):
    resto = n[cont] % 2
    if resto == 0:
        print(n[cont], end=' ')
