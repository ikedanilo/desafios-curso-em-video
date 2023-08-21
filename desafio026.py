# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece pela primeira vez
# - Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra "A" aparece {} vezes na frase'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na posição {} da frase'.format(frase.find('a')+1))
print('A letra "A" aparece pela última vez na posição {} da frase'.format(frase.rfind('a')+1))