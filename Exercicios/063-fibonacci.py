# 063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci:

n = int(input('Quantos elementos de fibonacci você deseja obter: '))

f0 = 0
f1 = 1
print(f'{f0} - {f1}', end = ' - ')

for c in range(3, n+1):
  f2 = f1+f0 
  f0 = f1
  f1=f2 
  if c!=n: 
    print(f2, end = ' - ')
  else:
    print(f2, end = ' ')
