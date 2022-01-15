# 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite um número inteiro: '))

escolha = int(input('Digite o número que corresponde a conversão que deseja fazer: (1) Binário, (2) Octal, (3) Hexadecimal '))

if escolha ==1:
  print(f'O número {num} convertido para binário é igual a {bin(num)}')
elif escolha ==2:
  print(f'O número {num} convertido para octal é igual a {oct(num)}')
elif escolha ==3:
  print(f'O número {num} convertido para hexadecimal é igual a {hex(num)}')
else:
  print('Você não digitou uma opção válida. ')