''' Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

numero = int(input('Digite um número inteiro: '))
print('*-*-' * 10)
print('Digite qual operação deseja realizar:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('Opção: '))

if opcao == 1:
    print('{} em binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em Octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} em Hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida')
