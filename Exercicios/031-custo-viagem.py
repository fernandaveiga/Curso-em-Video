# 031 - Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até
#200km e 0.45 para viagens mais longas:

dis = float(input(f'Digite a distancia da viagem: '))

if dis <=200.0:
  print(f'O valor da passagem é igual a {dis*0.5}')
else:
  print(f'O valor da passagem é igual a {dis*0.45}')