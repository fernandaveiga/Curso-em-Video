# 035 - Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo:

lista = []

for c in range(1,4):
  reta = int(input(f'Digite o comprimento da reta {c}: '))
  lista.append(reta)

if ((lista[0]+lista[1])>lista[2]) and ((lista[0]+lista[2])>lista[1]) and ((lista[1]+lista[2])>lista[0]):
  print('Estas três retas podem formar um triângulo. ')
else:
  print('Essas três retas não podem formar um triângulo. ')
