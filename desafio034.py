# Pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para Salários superior a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

sal = float(input('Informe o salário: R$'))

if sal > 1250.00:
    sal = sal * 1.1
else:
    sal = sal * 1.15

print('Novo salário é de R${:.2f}'.format(sal))
