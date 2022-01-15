# 067 - faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
#quando o número solicitado for negativo

n = int(input('Digite um número: '))

while n>0:
  for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
  n = int(input('Digite um número: '))
