# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada:

n = int(input(f"digite um número para calcularmos toda a tabuada: "))

for i in range(1, 11):
  print(f'{i}x{n}={i*n}')