'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('----' * 10)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')
    print('----' * 10)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
