# 058 - Melhore o jogo do desafio 028 onde o comnputador vai pensar em número de 0 a 10. Só que agora o jogador vai tentar adivinhar 
#até acertar, mostrando no final quantos palpites foram necessários para vencer:

from random import randint

n = 11
escolhido = randint(0,10)
count = 0

while n!=escolhido: 
  n = int(input('Tente adivinhar qual número entre 0 a 5 que o computador escolheu: '))
  count = count+1

print(f'Você escolheu {n} e o computador escolheu {escolhido}')
print(f'Você tentou {count} vezes até acertar ')