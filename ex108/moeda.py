def metade(num=0):
    res = num/2
    return res


def aumento(num=0, taxa=0):
    res = num + num * taxa/100
    return res


def diminuir(num=0, taxa=0):
    res = num - num * taxa/100
    return res


def dobro(num=0):
    res = num * 2
    return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')
