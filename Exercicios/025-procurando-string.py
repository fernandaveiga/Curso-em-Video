# 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome:

nome = str(input('Digite o nome completo: '))

nome = nome.lower()

if 'silva' in nome:
  print(f'Há Silva no nome {nome}')
else:
  print(f'Não há Silva no nome {nome}')