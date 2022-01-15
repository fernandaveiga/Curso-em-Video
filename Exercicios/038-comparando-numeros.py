# 038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Os valores são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1>n2:
  print(f'O primeiro número é maior. ')
elif n1==n2:
  print(f'O primeiro e segundo número são iguais. ')
else:
  print(f'O segundo número é maior')