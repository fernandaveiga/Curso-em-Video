# 061 - refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA usando while:

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))

n=primeiro
print(primeiro, end = ' ')
while n<(primeiro+(razao*9)):
  n = n+razao
  print(n, end = ' ')