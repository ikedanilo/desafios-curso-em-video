'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
 Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
time = ('Palmeiras', 'São Paulo', 'Corinthians', 'Santos', 'Flamengo', 'Vasco', 'Botafogo', 'Coritiba',
                 'Chapecoense', 'Sport', 'Londrina', 'Atlético MG', 'Atlético PR', 'Figueirense', 'Cruzeiro')
print('=-' * 40)
print(f'Os 5 primeiros colocados são: {time[0:5]}')
print('=-' * 40)
print(f'Os 4 últimos colocados são: {time[-4:]}')
print('=-' * 40)
print(f'Times em ordem alfabética: {sorted(time)}')
print('=-' * 40)
print(f'A Chape está na {time.index("Chapecoense")+1}ª posição')
