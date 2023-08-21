'''Refaça o desafio 32 adicionando as condições de qual triângulo será formado:
- Equilátero
- Isósceles
- Escaleno'''

from math import fabs

a = float(input('Digite o tamanho do lado a: '))
b = float(input('Digite o tamanho do lado b: '))
c = float(input('Digite o tamanho do lado c: '))

if fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b:
    print('É possível formar Triângulo!')
    if a == b == c:
        print('Triângulo é equilátero!')
    elif a == b or a == c or b == c:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não forma triângulo...')