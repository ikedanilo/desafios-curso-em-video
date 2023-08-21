'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
 e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
  mostre os valores pares e ímpares em ordem crescente.'''
lista = [[], []] #parte da esquerda é PAR. Direita é ÍMPAR
valor = 0
for cont in range(1, 8):
    valor = int(input(f'Digite o {cont}o. valor: '))
    if valor % 2 == 0: # Se for PAR coloca na lista da esquerda
        lista[0].append(valor)
    else:              # Se for ÍMPAR coloca na lista da direita
        lista[1].append(valor)
print('*-'*30)
lista[0].sort()
lista[1].sort()
print(f'A lista completa é: {lista}')
print(f'A lista dos valores pares é: {lista[0]}')
print(f'A lista dos valores ímpares é: {lista[1]}')
