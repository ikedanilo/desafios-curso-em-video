'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
 e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
  cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
temp = list()
boletim = list()
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append((nota1 + nota2) / 2)
    boletim.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('=-'*30)
print('{:^2} {:<8} {:<2}'.format('No.', 'NOME', 'MÉDIA'))
print('--'*10)
for i, v in enumerate(boletim):
    print(f'{i:^2} {v[0]:<10} {v[3]:.1f}')
print('--'*30)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opcao == 999:
        break
    elif opcao <= len(boletim) - 1:
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1:3]}')
        print('--' * 30)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')
