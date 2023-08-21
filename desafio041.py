'''A Confederação nacional de natação quer que de acordo com o ano de nascimento
de um atleta, seja classificada na categoria indicada:
- até 9 anos MIRIM
- Até 14 anos INFANTIL
- Até 19 anos JUNIOR
- Até 20 anos SENIOR
- Acima de 20 anos MASTER'''

from datetime import date

anoatual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = anoatual - ano

print('*-*-' * 10)
if idade < 9:
    print('Idade: {}\nCategoria: MIRIM'.format(idade))
elif 10 <= idade <= 14:
    print('Idade: {}\nCategoria: INFANTIL'.format(idade))
elif 15 <= idade <= 19:
    print('Idade: {}\nCategoria: JÚNIOR'.format(idade))
elif idade == 20:
    print('Idade: {}\nCategoria: SÊNIOR'.format(idade))
else:
    print('Idade: {}\nCategoria: MASTER'.format(idade))
