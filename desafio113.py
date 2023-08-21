''' Desafio 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número inválido. Aproveite e crie também uma função
leiaFloat() com a mesma funcionalidade.
'''
def leiaint(msg):
    while True:
        n = str(input(msg))
        try:
            valor = int(n)
            break
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor


def leiafloat(msg):
    while True:
        n = str(input(msg))
        try:
            valor = float(n)
            break
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
        except:
            print('\033[31mERRO! Digite um número real válido.\033[m')
    return valor


#Programa Principal
n = leiaint('Digite um número inteiro: ')
m = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {m}.')
