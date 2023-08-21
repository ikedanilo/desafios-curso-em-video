''' Desafio 101: Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
def voto(nascimento):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nascimento
    if 18 <= idade <= 65:
        return f'Tem {idade} anos: VOTO OBRIGATORIO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Tem {idade} anos: VOTO OPCIONAL'
    else:
        return f'Tem {idade} anos: VOTO NEGADO'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
