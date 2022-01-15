# 042 - refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilatero, isosceles, escaleno:

l1 = int(input('Digite um lado: '))
l2 = int(input('Digite um segundo lado: '))
l3 = int(input('Digite um terceiro lado: '))

if ((l1+l2)>l3) and ((l1+l3)>l2) and ((l2+l3)>l1):
  print('Estas três retas podem formar um triângulo. ')
  if l1==l2==l3:
    print('Este triângulo é equilátero! ')
  elif (l1==l2) or (l2==l3) or (l3==l1):
    print('Este triângulo é isósceles! ')
  else:
    print('Este triângulo é escaleno! ')
else:
  print('Essas três retas não podem formar um triângulo. ')