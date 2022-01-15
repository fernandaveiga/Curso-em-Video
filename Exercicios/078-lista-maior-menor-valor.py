# 078 - Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor 
#digitado e suas respectivas posições na lista:

lista = []

for c in range(1,6):
  n = int(input('Digite um número: '))
  lista.append(n)

maximo = max(lista)
minimo = min(lista)

print(f'O maior valor foi {maximo} nas posições ', end = ' ')
for pos, item in enumerate(lista):
  if item==maximo:
    print(f'{pos+1}', end = ' ')
    print(' ... ', end = '')

print(f'o menor valor foi {minimo} nas posições', end = ' ')
for pos, item in enumerate(lista):
  if item==minimo:
    print(f'{pos+1}', end = ' ')
    print(' ... ' , end = '')
