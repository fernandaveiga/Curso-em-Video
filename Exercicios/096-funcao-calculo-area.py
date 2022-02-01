# 096 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retângular (largura e comprimento) e 
#mostre a área do terreno

print('-'*24)
print('--CONTROLE DE TERRENOS--')
print('-'*24)

def cterrenos(l, c):
  print(f'A área do terreno {l}x{c} é igual a {l*c} m².')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
cterrenos(l,c)