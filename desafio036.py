''' Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode exceder
30% do salário ou então o empréstimo será negado'''

casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos pretende quitar a casa: '))

prest = casa / (anos * 12)

if prest > salario * 0.3:
    print('Empréstimo negado... Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} sendo que'
          ' 30% do salário é {:.2f}.'.format(casa, anos, prest, salario * 0.3))
else:
    print('Empréstimo aceito! Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'
          .format(casa, anos, prest))
