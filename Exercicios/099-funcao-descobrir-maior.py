# 099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analizar todos os
#valores e dizer qual deles é o maior.

def maior(*n):
  if len(n)>0:
    count = 0
    for c in n:
      count = count+1
    print(f'Foram informados {count} valores')
    print(f'O maior valor é: {max(n)}')
  else:
    print(f'Foram informados 0 valores')
    print(f'Não tem valor máximo')
  print('-'*26)

maior(2,6,8,9,0,2)
maior(11, 45, 98, 103, 56)
maior()