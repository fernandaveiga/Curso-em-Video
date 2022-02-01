# 088 - Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista: 

from random import randint

n = int(input('Quantos jogos você deseja sortear? '))

for c in range(1, n+1):
  lista = []
  d=1
  while d<=6:
    j = randint(1,60)
    if j not in lista:
      lista.append(j)
      d=d+1
  print(f'Jogo {c}: {lista}')
print('BOA SORTE!')
