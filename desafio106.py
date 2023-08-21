''' Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
o programa se encerrará. Importante: use cores. '''
def funcao(msg):
    help(msg)

def titulo(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)


#Programa Principal
while True:
    titulo('Sistema de ajuda PyHelp')
    resp = str(input('Função ou Biblioteca: ')).strip().lower()
    if resp in 'fim':
        break
    else:
        funcao(resp)
titulo('Até Logo!')
