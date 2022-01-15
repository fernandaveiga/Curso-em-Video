# 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
#militar, se é a hora de se alistar ou se já passou da hora de se alistar. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo:

from datetime import datetime

nasc = int(input('Digite o ano de nascimento: '))
data_atual = datetime.now()
data_atual = str(data_atual)
data_atual = data_atual.replace('-', ' ')
data_atual = data_atual.split()
ano_atual = data_atual[0]
print(ano_atual)

idade = int(ano_atual) - nasc

if idade == 18:
  print(f'A idade é 18, está na hora de se alistar! ')
elif idade < 18:
  print(f'A idade é {idade}, {18-idade} anos para se alistar! ')
else:
  print(f'A idade é {idade}, {idade-18} atrasados para o alistamento! ')
