# 089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo 
#a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = []

while True:
  nome = input('Digite o nome: ')
  n1 = float(input('Digite a primeira nota: '))
  n2 = float(input('Digite a segunda nota: '))
  listam.append(media)
  lista.append([nome, [n1, n2], media])
  resp = input('Deseja continuar? [S ou N] ')
  if resp not in 'Ss':
    break

print(f"{'N°':<4} {'Nome':<10} {'Média':>8}")
for pos, item in enumerate(lista):
  print(f'{pos:<4} {lista[pos][0]:<10} {lista[pos][2]:>8.1f}')
