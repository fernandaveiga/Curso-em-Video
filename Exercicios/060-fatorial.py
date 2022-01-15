# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial:

num = int(input('Digite um número: '))
fat = 1
while num>1:
  print(f'{num}x', end = '')
  fat = fat*num
  num = num-1
print(f'1={fat}')
