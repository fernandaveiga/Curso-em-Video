# 066 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o número 999.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles:

resp = 1
count = 0
soma = 0

while resp != 999:
  resp = int(input('Digite um número inteiro: '))
  count = count+1
  soma = soma+resp

print(f'Foram digitados {count-1} números e a soma foi {soma-999} ')