#Desafio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao toda (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip()

print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))

dividido = nome.split()
print('Quantidade de letras sem espaço no nome: {}'.format(len(dividido[0]) + len(dividido[1]) + len(dividido[2])))
print('Quantidade de letras no primeiro nome: {}'.format(len(dividido[0])))