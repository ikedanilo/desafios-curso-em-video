'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS IKEDA '))

preco = float(input('Digite o preço normal do produto: R$'))

print('''*** Escolha a forma de pagamento abaixo ***
[1] - à vista dinheiro/cheque:
[2] - à vista no cartão
[3] - em até 2x no cartão:
[4] - 3x ou mais no cartão:''')

opcao = int(input('Escolhe a opção: '))

if opcao == 1:
    novopreco = preco * 0.9
elif opcao == 2:
    novopreco = preco * 0.95
elif opcao == 3:
    novopreco = preco
    print('Sua compra será parcelada 2x de R${:.2f} SEM JUROS'.format(novopreco/2))
elif opcao == 4:
    novopreco = preco * 1.2
    parcela = int(input('Quantidade de parcelas: '))
    if parcela >= 3:
        print('Sua compra será parcelada {}x de R${:.2f} COM JUROS'.format(parcela, novopreco/parcela))

if 1 <= opcao <= 4:
    if opcao == 4 and parcela < 3:
        print('Valor de parcelamento inválido. Para esta opção as parcelas devem ser maiores que 3x.')
    else:
        print('Sua compra de R${:.2f} irá custar R${:.2f} no final.'.format(preco, novopreco))
else:
    print('Opção inválida.')
