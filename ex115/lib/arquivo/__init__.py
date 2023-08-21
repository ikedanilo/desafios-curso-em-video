from ex115.lib.interface import *  #importando do interface


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # Open = tenta abrir o arquivo / rt = READ
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # wt = Escreve um arquivo, o sinal '+' significa que caso ele não exista ele cria o arq.
        a.close()  #Fecha o arquivo
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.read())  # Lê o arquivo inteiro da maneira como ele está escrito
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome, idade):
    try:
        a = open(arq, 'at')  # at = append -> inserir dados no arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever o arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
