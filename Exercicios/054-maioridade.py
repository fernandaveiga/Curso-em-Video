# 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
#quantas já são maiores:

from datetime import date
atual = date.today().year
count =0

for c in range(1, 8):
  nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
  if atual - nasc<18:
    count = count+1

print(f'{count} pessoas dessa lista não atingiram a maioridade. ')
