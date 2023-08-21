''' Melhore o jogo do Desafio 2018 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

n = 1
tent = 0
c = randint(0, 5)

print('Sou seu computador...pensei em um número. Será que você consegue adivinhar?')

while n != c:
    n = int(input('Digite um número entre 0 e 5: '))
    tent += 1
    print('PROCESSANDO...')
    sleep(2)

    if n == c:
        print('Você venceu na {}ª tentativa! O número do computador foi {} e o seu foi {}'.format(tent, c, n))
    elif c > n:
        print('Mais...escolha um número maior que {}'.format(n))
    elif c < n:
        print('Menos...escolha um número menor que {}'.format(n))

print('*** FIM ***')
