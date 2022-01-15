# 032 - Faça um programa que leia um ano qualquer bissexto:

ano = int(input('Digite o ano: '))

if ano%4==0:
  print('{ano} é bissexto! ')
else:
  print('{ano} não é bissexto! ')