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
