# 090 - Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.

dicio = {}

dicio['nome'] = input('Digite o nome: ')
dicio['media'] = float(input('Digite a média: '))
if dicio['media']<4.0:
  dicio['Situação']='Reprovado'
if (dicio['media']>=4.0) and (dicio['media']<6.0):
  dicio['Situação'] = 'Recuperação'
if (dicio['media']>=6):
  dicio['Situação'] = 'Aprovado'

print(f"O nome é igual a {dicio['nome']}")
print(f"A média é igual a {dicio['media']}")
print(f"A situação é igual a {dicio['Situação']}")