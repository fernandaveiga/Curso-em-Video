# 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada:

import random
from random import shuffle
lista = []

for c in range(1,5):
  nome = str(input(f'Digite o nome do aluno {c}: '))
  lista.append(nome)

print(lista)
random.shuffle(lista)
print(lista)
