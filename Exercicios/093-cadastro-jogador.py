# 093 - Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
#vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

lista = []
dicio = {}

nome = input('Digite o nome: ')
dicio['nome'] = nome
n = int(input(f'Digite o número de partidas que o {nome} jogou: '))
dicio['partidas'] = n

for c in range(1, n+1):
  gol = int(input(f'Quantos gols o {nome} fez na partida {c}? '))
  lista.append(gol)
dicio['gols']=lista
dicio['tgols'] = sum(lista)

print(dicio)
print(' ')
print(f'''{dicio['nome'].capitalize()} jogou {dicio['partidas']} partidas e fez {dicio['tgols']} gols.''')
print(' ')
for pos, item in enumerate(lista):
  print(f'Na partida {pos+1}, fez {item} gols.')
