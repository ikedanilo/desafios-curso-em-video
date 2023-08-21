'''Faça um programa que tenha uma FUNÇÃO chamada escreva() que receba um texto qualquer como
PARÂMETRO e mostre uma mensagem com tamanho adaptável.'''

def escreva(txt):
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))


#Programa Principal
escreva('Danilo Messias Ikeda')
escreva('Olá Mundo!')
escreva('Bem vindo ao Curso de Python 3!')
