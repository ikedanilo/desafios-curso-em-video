'''Crie um programa que leia uma frase qualquer e diga se
ela é um palindromo, desaconsiderando os espaços
ex:
apos a sopa
a sacada da casa
a torre da derrota
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('{} e {} é palindromo'.format(inverso, junto))
else:
    print('{} e {} NÃO é palindromo'.format(inverso, junto))
