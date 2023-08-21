'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
boletim = dict()
boletim['nome'] = str(input('Nome: ')).upper()  #Ler key Nome no dicionário
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))    #Ler key MEDIA no dicionário
if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'
print('-='*20)
for k, v in boletim.items(): #Imprimir dicionário (key e value)
    print(f'- {k} é igual a {v}')
