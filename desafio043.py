'''Leia o peso e altura de uma pessoa e calcule o IMC e
classifique:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

alt = float(input('Digite a sua altura (m): '))
peso = float(input('Digite o seu peso (kg): '))

imc = peso / pow(alt, 2)

if imc < 18.5:
    print('IMC: {:.2f} - Abaixo do Peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC: {:.2f} - Peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC: {:.2f} - Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('IMC: {:.2f} - Obesidade'.format(imc))
else:
    print('IMC: {:.2f} - Obesidade mórbida'.format(imc))
