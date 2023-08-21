def leiaInt(msg):
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


def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))  # .center() centraliza o texto
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc
