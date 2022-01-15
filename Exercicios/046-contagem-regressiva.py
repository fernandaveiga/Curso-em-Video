# 046 - Faça um programa que mostre na tela uma contagem regressiva, indo de 10 a 0, com pausa de 1s entre eles.

from time import sleep

for c in range(10, -1, -1):
  print(c)
  sleep(1)
print('BOOM')