# Escreva um programa que faça o computador "pensar". Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

n = int(input('Digite um número entre 0 e 5: '))

c = randint(0, 5)

print('PROCESSANDO...')
sleep(3)

if n == c:
    print('Você venceu! O número do computador foi {} e o seu foi {}'.format(c, n))
else:
    print('Você perdeu. Você escolheu {} e o computador {}'.format(n, c))
print('*** FIM ***')
