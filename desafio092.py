'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''
from datetime import datetime #Importar biblioteca para trazer ANO ATUAL
funcionario = dict()
funcionario['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
funcionario['idade'] = datetime.now().year - nascimento #conta para calcular a idade da pessoa
funcionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if funcionario['ctps'] != 0:
    funcionario['contratacao'] = int(input('Ano de Contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['contratacao'] + 35 - nascimento
print('-='*20)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}.')
