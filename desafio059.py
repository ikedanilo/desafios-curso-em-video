''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar cada operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor : '))

opcao = 0

while opcao != 5:
    print('**** MENU ****\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Saber qual é o Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('Soma: {} + {} = {}'.format(n1, n2, soma))
        print('----' * 10)
    elif opcao == 2:
        mult = n1 * n2
        print('Multiplicação: {} * {} = {}'.format(n1, n2, mult))
        print('----' * 10)
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
        print('----' * 10)
    if opcao == 4:
        print('Novos números!')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor : '))
        print('----' * 10)
print('*** FIM DO PROGRAMA ***')
