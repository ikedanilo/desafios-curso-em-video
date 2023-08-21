def metade(num=0, formato=False):
    res = num/2
    return res if formato is False else moeda(res)


def aumento(num=0, taxa=0, formato=False):
    res = num + num * taxa/100
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - num * taxa/100
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')


def resumo(preco, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DOS DADOS'.center(30)) #centralizado em 30 caracteres
    print('-' * 30)
    print(f'Analisando valor: \t{moeda(preco)}') #Tabulação joga tudo pra direita deixando alinhados
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Aumento de {taxaa}%: \t{aumento(preco, taxaa, True)}')
    print(f'Diminuição de {taxar}%: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
