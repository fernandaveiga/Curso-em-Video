# 051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa PA:

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

for c in range(primeiro, primeiro+(10*razao), razao):
  print(c, end = ' ')