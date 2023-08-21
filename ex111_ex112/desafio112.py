#Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz
# de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que seja monetários.

from ex111_ex112.utilidadesCeV import moeda #Import do pacote moeda
from ex111_ex112.utilidadesCeV import dado #Import do pacote dado

p = dado.leiaDinheiro('Digite um preço : R$')
moeda.resumo(p, 20, 12)
