# 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))
if velocidade>80.0:
  print('Você foi multado!')
  multa = (velocidade-80.0)*7
  print(f'O valor da multa é: R${multa}')
else:
  print('Velocidade permitida! Tenha um bom dia!')