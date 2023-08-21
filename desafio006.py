# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# Vídeo: Exercício Python #006 - Dobro, Triplo, Raiz Quadrada

n = int(input('Digite um número: '))

print('Dobro de {} é {} \nTriplo de {} é {} e\nA raiz quadrada de {} é {:.2f}'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))
