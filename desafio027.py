# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o último nome
# separadamente

nome = str(input('Digite o nome completo: ')).strip().title()

dividido = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
