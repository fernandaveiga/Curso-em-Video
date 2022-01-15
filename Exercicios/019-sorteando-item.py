# 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
#lendo o nome deles e escrevendo o nome do escolhido: 

from random import randint 

dicio = {}
for c in range(1,5):
  nome = str(input(f'Digite o nome do aluno {c}: '))
  dicio[c] = nome

num_escolhido = randint(1,4)

print(f'O número escolhido foi {num_escolhido} e o nome é {dicio[num_escolhido]}')
