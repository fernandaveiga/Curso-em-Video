# 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Aguarde esses resultados em um dicionário. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
dicio = {}

for c in range(1, 5):
  n = randint(1,6)
  dicio[c]=n

for k, v in dicio.items():
  print(f'O jogador {k} tirou {v} do dado. ')
  sleep(0.5)
print(' ')

for item in sorted(dicio, key = dicio.get, reverse = True):
  print(f'Em ordem do maior para o menor, temos: o jogador {item} tirou {dicio[item]}')
  sleep(0.5)
