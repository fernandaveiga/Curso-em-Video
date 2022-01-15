# 028 - Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

escolhido = randint(0,5)
n = int(input('Tente adivinhar qual núnero entre 0 a 5 que o computador escolheu: '))

print(f'Você escolheu {n} e o computador escolheu {escolhido}')
if n==escolhido:
  print('Você acertou! (: ')
else:
  print('Você errou ): ')