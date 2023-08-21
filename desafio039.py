'''Faça um programa que leia o ano de nascimento de um jovem
e informe de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de alistamento
Seu programa deverá mostrar o tempo que falta ou que passou do prazo
'''

from datetime import date

anoatual = date.today().year
nasc = int(input('Digite o ano que você nasceu: '))
idade = anoatual - nasc

if idade == 18:
    print('Você tem {} anos. Se fodeu! Se aliste no exército agora!'.format(idade))
elif 0 <= idade < 18:
    print('Você tem {} anos. Você vai se alistar no exército daqui {} ano(s) em {}'
          .format(idade, 18 - idade, anoatual + (18 - idade)))
elif idade > 18:
    print('Você tem {} anos. Você já passou do tempo de alistamento faz {} ano(s).'
          ' Seu alistamento foi em {}'
          .format(idade, idade - 18, anoatual - (idade - 18)))
elif idade < 0:
    print('Você veio do futuro.')
