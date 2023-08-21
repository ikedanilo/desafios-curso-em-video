# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho
# de alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

a1 = str(input("Nome Aluno 1: "))
a2 = str(input("Nome Aluno 2: "))
a3 = str(input("Nome Aluno 3: "))
a4 = str(input("Nome Aluno 4: "))

lista = [a1, a2, a3, a4]
shuffle(lista)

print("A ordem de apresentação é:")
print(lista)