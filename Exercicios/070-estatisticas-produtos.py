# 070 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#a - O total de gastos da compra
#b - Quantos produtos custam mais de 1000
#c - Qual é o nome do produto mais barato

tp = 0
c1000 = 0
resp = 'S'
menor = 0
count = 0

while resp=='S':
  nome = input('Digite o nome do produto: ')
  preco = float(input('Digite o preço do produto: '))
  count = count+1
  if count==1:
    menor=preco
    barato=nome
  else:
    if preco<menor:
      menor=preco
      barato = nome
  tp = tp+preco
  if preco>1000:
    c1000 = c1000+1
  resp = str(input('Deseja continuar a adicionar produtos? [S ou N] ')).upper()

print(f'O total de gastos nesta compra foi {tp}')
print(f'{c1000} produtos custam mais de R$1000')
print(f'O menor preço é {menor} do produto {barato}')