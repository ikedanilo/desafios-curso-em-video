# Um professor quer sortear um de seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome do escolhido

from random import choice

a1 = str(input("Nome Aluno 1: "))
a2 = str(input("Nome Aluno 2: "))
a3 = str(input("Nome Aluno 3: "))
a4 = str(input("Nome Aluno 4: "))

lista = [a1, a2, a3, a4]

sorteado = choice(lista)

print("O aluno escolhido randomicamente para apagar o quadro é {}".format(sorteado))