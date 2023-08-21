'''Digite 2 notas e faça a média. Se o aluno teve:
- menor que 5 - Reprovado
- media entre 5 e 6.9 - Recuperação
- acima de 7 - aprovado'''

n1 = float(input('Digite a nota da p1: '))
n2 = float(input('Digite a nota da p2: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Média = {:.2f} - APROVADO'.format(media))
elif media < 5:
    print('Média = {:.2f} - REPROVADO'.format(media))
else:
    print('Média = {:.2f} - RECUPERAÇÃO'.format(media))
