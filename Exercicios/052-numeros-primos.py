# 052 - Faça um programa que lê um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
lista = []

for c in range(num-1, 1, -1):
  (lista).append(num%c)

if 0 not in lista:
  print('Este número é primo! ')
else:
  print('Este número não é primo! ')